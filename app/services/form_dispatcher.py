# همه حتی 8 تا فرم

from app.config.form_configs import SERVICE_MAP as LEGACY_SERVICE_MAP

from app.config.dynamic_form_configs import (
    SERVICE_MAP as DYNAMIC_SERVICE_MAP
)
from app.services.dynamic_form_service import (
    get_rows_dynamic_form,
    save_rows_dynamic_form
)
from app.services.generic_form_service import (
    get_rows_generic_form,
    save_rows_generic_form
)
from app.models.form_permission import (
    FormPermission
)
SERVICE_MAP = {
    **LEGACY_SERVICE_MAP,
    **DYNAMIC_SERVICE_MAP
}
def get_rows_generic(form_key, **kwargs):

    config = SERVICE_MAP.get(form_key)

    if not config:
        raise Exception("Unknown form")

    if config.get("type") == "dynamic":

        return get_rows_dynamic_form(
            config=config,
            **kwargs
        )

    return get_rows_generic_form(
        config=config,
        **kwargs
    )

def save_rows_generic(form_key, **kwargs):

    config = SERVICE_MAP.get(form_key)

    if not config:
        raise Exception("Unknown form")

    if config.get("type") == "dynamic":

        return save_rows_dynamic_form(
            config=config,
            **kwargs
        )

    return save_rows_generic_form(
        config=config,
        **kwargs
    )

def get_form_meta(form_key):

    service = SERVICE_MAP.get(form_key)

    if not service:
        raise Exception("Unknown form")

    meta = service["meta"].copy()

    meta["type"] = "dynamic" if "columns" in service else "generic"

    if "columns" in service:
        meta["columns"] = service["columns"]

    return meta




def get_forms_menu(
    db,
    current_user
):

    groups = {}

    for key, config in SERVICE_MAP.items():

        group = config.get("menu_group")
        title = config.get("menu_title")

        if not group or not title:
            continue

        allowed = False

        # ادمین همه فرم‌ها را می‌بیند
        if (
            current_user.role and
            current_user.role.name
            in ["ADMIN", "ADMINISTRATOR"]
        ):
            allowed = True

        else:

            companies = [
                c.company_name
                for c in current_user.companies
            ]

            permission = (
                db.query(FormPermission)
                .filter(
                    FormPermission.form_key == key,
                    FormPermission.company.in_(
                        companies
                    ),
                    FormPermission.is_enabled == True
                )
                .first()
            )

            if permission:
                allowed = True

        if not allowed:
            continue

        if group not in groups:
            groups[group] = []

        groups[group].append({
            "key": key,
            "title": title
        })

    result = []

    for group_name, items in groups.items():

        result.append({
            "group": group_name,
            "items": items
        })

    return result