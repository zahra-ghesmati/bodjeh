from fastapi import HTTPException
import re

from app.services.access_service import (
    check_access,
    is_period_locked
)
from app.models.form_permission import (
    FormPermission
)
def check_form_permission(
    db,
    form_key,
    company
):

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

        raise HTTPException(
            status_code=403,
            detail="این فرم برای شرکت فعال نیست"
        )
def validate_year(year):

    if not re.match(
        r"^\d{4}-\d{4}$",
        year
    ):

        raise HTTPException(
            status_code=400,
            detail=f"فرمت سال مالی '{year}' نامعتبر است."
        )
def build_template(
    db,
    company,
    config
):

    Model = config["model"]

    latest_year = (
        db.query(Model.sal_maly)
        .filter(
            Model.nam_shrkt == company
        )
        .distinct()
        .order_by(
            Model.sal_maly.desc()
        )
        .first()
    )

    if not latest_year:
        return []

    fields = config.get(
        "template_distinct_fields",
        []
    )

    if not fields:
        return []

    query_fields = [
        getattr(Model, f)
        for f in fields
    ]

    rows = (
        db.query(*query_fields)
        .filter(
            Model.nam_shrkt == company,
            Model.sal_maly == latest_year[0]
        )
        .distinct()
        .all()
    )

    result = []

    for row in rows:

        item = {
            "id": None,
            "budget": None,
            "actual": None
        }

        if len(row) > 0:
            item["dimension1"] = row[0]

        if len(row) > 1:
            item["dimension2"] = row[1]

        if len(row) > 2:
            item["dimension3"] = row[2]

        result.append(item)

    return result
# =========================
# GET
# =========================
def get_rows_generic_form(
    config,
    db,
    company,
    year,
    month,
    current_user
):
    validate_year(year)
    check_access(
        db,
        current_user,
        company
    )
    check_form_permission(
        db,
        config["form_key"],
        company
    )
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

    if not rows:
        return build_template(
        db,
        company,
        config
    )

    result = []

    for r in rows:

        item = {
            "id": r.id,
            "budget":
                getattr(
                    r,
                    config["budget_field"]
                ),
            "actual":
                getattr(
                    r,
                    config["actual_field"]
                )
        }

        if "dimension1_field" in config:
            item["dimension1"] = getattr(
                r,
                config["dimension1_field"]
            )

        if "dimension2_field" in config:
            item["dimension2"] = getattr(
                r,
                config["dimension2_field"]
            )

        if "dimension3_field" in config:
            item["dimension3"] = getattr(
                r,
                config["dimension3_field"]
            )

        result.append(item)

    return result


# =========================
# SAVE
# =========================
def normalize_text(value):
    if not value:
        return None

    return (
        value
        .strip()
      
    )
def save_rows_generic_form(
    config,
    db,
    payload,
    current_user
):
    validate_year(
        payload.year
    )
    check_access(
        db,
        current_user,
        payload.company
    )
    check_form_permission(
        db,
        config["form_key"],
        payload.company
    )
    Model = config["model"]

    budget_locked = is_period_locked(
        db,
        config["form_key"],
        payload.company,
        payload.year,
        payload.month,
        "budget"
    )


    actual_locked = is_period_locked(
        db,
        config["form_key"],
        payload.company,
        payload.year,
        payload.month,
        "actual"
    )
    if budget_locked and actual_locked:
        raise HTTPException(
            status_code=403,
            detail="این دوره تایید نهایی شده و قابل ویرایش نیست."
        )
    try:
        order_map = None


        if Model.__name__ == "AmountRowMaterialCnsumtion":
            #فقط برای فرم مقدار مصرف مواد اولیه/چون نیاز به ردیف با مقدار خاص دارد
            order_map = {

                ("آهک", "خاکستري"): 1,
                ("مارل", "خاکستري"): 2,
                ("آهن", "خاکستري"): 3,
                ("سيليس", "خاکستري"): 4,
                ("بوکسيت", "خاکستري"): 5,
                ("ساير مواد مصرفي (مرحله پخت)", "خاکستري"): 6,
                ("سرباره", "خاکستري"): 7,
                ("پوزولان", "خاکستري"): 8,
                ("گچ", "خاکستري"): 9,
                ("آهک افزودني", "خاکستري"): 10,
                ("ساير افزودني ها", "خاکستري"): 11,
                ("کلينکر خريداري شده", "خاکستري"): 12,
                ("کلينکر خريداري شده مصرفي", "خاکستري"): 12,
                ("تفاوت موجودي ابتدا و پايان دوره سيلوهاي مواد خام", "خاکستري"): 13,

                ("آهک", "سفيد"): 14,
                ("کائولن", "سفيد"): 15,
                ("فلد اسپات", "سفيد"): 16,
                ("گچ", "سفيد"): 17,
                ("ساير افزودني ها", "سفيد"): 18,
                ("کلينکر خريداري شده", "سفيد"): 19,
                ("تفاوت موجودي ابتدا و پايان دوره سيلوهاي مواد خام", "سفيد"): 20,

                }


        for row in payload.rows:

            existing = None

            if row.id:

                existing = (
                    db.query(Model)
                    .filter(
                        Model.id == row.id
                    )
                    .first()
                )

            if existing:

                if not budget_locked:

                    setattr(
                        existing,
                        config["budget_field"],
                        row.budget
                    )

                if not actual_locked:

                    setattr(
                        existing,
                        config["actual_field"],
                        row.actual
                    )

                if Model.__name__ == "AmountRowMaterialCnsumtion":
                 #فقط برای فرم مقدار مصرف مواد اولیه/چون نیاز به ردیف با مقدار خاص دارد

                    existing.rdyf = order_map.get(
                        (
                            normalize_text(row.dimension1),
                            normalize_text(row.dimension2)
                        )
                    )
                    if existing.rdyf is None:
                        raise Exception(
                            f"ردیف تعریف نشده برای {row.dimension1} - {row.dimension2}"
                        )
            else:

                obj = Model(
                    nam_shrkt=
                        payload.company,

                    sal_maly=
                        payload.year,

                    mah_zarsh=
                        payload.month
                )
  

                if "dimension1_field" in config:
                    setattr(
                        obj,
                        config["dimension1_field"],
                        row.dimension1
                    )

                if "dimension2_field" in config:
                    setattr(
                        obj,
                        config["dimension2_field"],
                        row.dimension2
                    )

                if "dimension3_field" in config:
                    setattr(
                        obj,
                        config["dimension3_field"],
                        row.dimension3
                    )

                setattr(
                    obj,
                    config["budget_field"],
                    None if budget_locked else row.budget
                )

                setattr(
                    obj,
                    config["actual_field"],
                    None if actual_locked else row.actual
                )

                if Model.__name__ == "AmountRowMaterialCnsumtion":
                    #فقط برای فرم مقدار مصرف مواد اولیه/چون نیاز به ردیف با مقدار خاص دارد

                    obj.rdyf = order_map.get(
                        (
                            normalize_text(row.dimension1),
                            normalize_text(row.dimension2)
                        )
                    )
                    if obj.rdyf is None:
                        raise Exception(
                            f"ردیف تعریف نشده برای {row.dimension1} - {row.dimension2}"
                        )  
                db.add(obj)

        db.commit()

        return {
            "status": "success"
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )