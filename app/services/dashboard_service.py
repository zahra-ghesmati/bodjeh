from app.config.form_configs import SERVICE_MAP
from app.models.report_confirmation import PeriodLock

from app.services.access_service import (
    check_access
)

from app.models.form_permission import (
    FormPermission
)
def has_value(v):

    if v is None:
        return False

    if isinstance(v, str):
        return bool(v.strip())

    return True


def calculate_status(
    rows,
    field_name,
    approved
):

    if approved:
        return "closed"

    if not rows:
        return "not_started"

    values = [
        getattr(row, field_name, None)
        for row in rows
    ]

    filled_count = sum(
        1
        for v in values
        if has_value(v)
    )

    if filled_count == 0:
        return "not_started"

    if filled_count < len(values):
        return "incomplete"

    return "completed"


def get_dashboard_status(
    db,
    company,
    year,
    month,
    current_user
):

    check_access(
        db,
        current_user,
        company
    )

    result = []

    for form_key, config in SERVICE_MAP.items():
        permission = (
            db.query(FormPermission)
            .filter(
                FormPermission.form_key == form_key,
                FormPermission.company == company,
                FormPermission.is_enabled == True
            )
            .first()
        )

        if not permission:
            continue

        try:

            Model = config["model"]

            rows = (
                db.query(Model)
                .filter(
                    Model.nam_shrkt == company,
                    Model.sal_maly == year,
                    Model.mah_zarsh == month
                )
                .all()
            )


            lock = (
                db.query(PeriodLock)
                .filter(
                    PeriodLock.form_key == form_key,
                    PeriodLock.company == company,
                    PeriodLock.sal_maly == year,
                    PeriodLock.mah == month
                )
                .first()
            )

            budget_status = calculate_status(
                rows,
                config["budget_field"],
                lock.budget_approved if lock else False
            )

            actual_status = calculate_status(
                rows,
                config["actual_field"],
                lock.actual_approved if lock else False
            )

            result.append({
                "form_key": form_key,
                "title": config["meta"]["title"],
                "group": config.get("menu_group"),
                "budget_status": budget_status,
                "actual_status": actual_status
            })

        except Exception as e:

            result.append({
                "form_key": form_key,
                "title": config["meta"]["title"],
                "group": config.get("menu_group"),
                "budget_status": "error",
                "actual_status": "error",
                "error": str(e)
            })

    return result




def get_admin_dashboard_status(
    db,
    year,
    month,
    current_user
):

    if current_user.role.name not in [
        "ADMIN",
        "ADMINISTRATOR"
    ]:
        raise Exception("Access denied")

    companies = (
        db.query(FormPermission.company)
        .distinct()
        .all()
    )

    result = []

    for company_row in companies:

        company = company_row[0]

        budget = {
            "not_started": 0,
            "incomplete": 0,
            "completed": 0,
            "closed": 0
        }

        actual = {
            "not_started": 0,
            "incomplete": 0,
            "completed": 0,
            "closed": 0
        }

        for form_key, config in SERVICE_MAP.items():

            permission = (
                db.query(FormPermission)
                .filter(
                    FormPermission.form_key == form_key,
                    FormPermission.company == company,
                    FormPermission.is_enabled == True
                )
                .first()
            )

            if not permission:
                continue

            Model = config["model"]

            rows = (
                db.query(Model)
                .filter(
                    Model.nam_shrkt == company,
                    Model.sal_maly == year,
                    Model.mah_zarsh == month
                )
                .all()
            )

            lock = (
                db.query(PeriodLock)
                .filter(
                    PeriodLock.form_key == form_key,
                    PeriodLock.company == company,
                    PeriodLock.sal_maly == year,
                    PeriodLock.mah == month
                )
                .first()
            )

            budget_status = calculate_status(
                rows,
                config["budget_field"],
                lock.budget_approved if lock else False
            )

            actual_status = calculate_status(
                rows,
                config["actual_field"],
                lock.actual_approved if lock else False
            )

            budget[budget_status] += 1
            actual[actual_status] += 1

        total_forms = sum(budget.values())

        completed_count = (
            budget["completed"]
            + budget["closed"]
            + actual["completed"]
            + actual["closed"]
        )

        progress = 0

        if total_forms > 0:

            progress = round(
                (
                    completed_count /
                    (total_forms * 2)
                ) * 100
            )

        result.append({
            "company": company,
            "budget": budget,
            "actual": actual,
            "progress": progress
        })

    return result