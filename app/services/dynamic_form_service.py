# 8 فرم

from fastapi import HTTPException

from app.services.access_service import (
    check_access,
)

from app.services.generic_form_service import (
    validate_year,
    check_form_permission,
)


def build_template_dynamic(
    db,
    company,
    config
):
    Model = config["model"]

    template_fields = config.get(
        "template_distinct_fields",
        []
    )

    if not template_fields:
        return []

    query_fields = [
        getattr(Model, field)
        for field in template_fields
    ]

    rows = (
        db.query(*query_fields)
        .filter(
            Model.nam_shrkt == company
        )
        .distinct()
        .all()
    )

    result = []

    for row in rows:

        values = {}

        for index, field in enumerate(
            template_fields
        ):
            values[field] = row[index]

        result.append(
            {
                "id": None,
                "values": values
            }
        )

    return result


def get_rows_dynamic_form(
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

    query = db.query(Model).filter(
        Model.nam_shrkt == company,
        Model.sal_maly == year
    )

    if hasattr(Model, "mah_zarsh"):
        query = query.filter(
            Model.mah_zarsh == month
        )

    rows = query.all()

    if not rows:

        if config.get(
            "load_template_if_empty",
            True
        ):
            return build_template_dynamic(
                db,
                company,
                config
            )

        return []

    result = []

    for row in rows:

        values = {}

        for col in config["columns"]:

            field = col["field"]

            values[field] = getattr(
                row,
                field
            )

        result.append(
            {
                "id": row.id,
                "values": values
            }
        )

    return result


def save_rows_dynamic_form(
    config,
    db,
    payload,
    current_user
):
    validate_year(payload.year)

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

    editable_fields = [
        col["field"]
        for col in config["columns"]
        if col.get(
            "editable",
            False
        )
    ]

    identity_fields = config.get(
        "identity_fields",
        []
    )

    try:

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

                for field in editable_fields:

                    if field in row.values:

                        setattr(
                            existing,
                            field,
                            row.values[field]
                        )

            else:

                obj = Model(
                    nam_shrkt=payload.company,
                    sal_maly=payload.year
                )

                if hasattr(
                    Model,
                    "mah_zarsh"
                ):
                    obj.mah_zarsh = (
                        payload.month
                    )

                for field, value in (
                    row.values.items()
                ):

                    setattr(
                        obj,
                        field,
                        value
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