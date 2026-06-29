from sqlalchemy.inspection import inspect
from app import models
from app.models import * # یا ایمپورت تک‌تک مدل‌ها



def get_model_schema(model):
    mapper = inspect(model)

    columns = []

    for column in mapper.columns:
        columns.append({
            "field": column.key,
            "label": column.name,
            "type": str(column.type),
            "is_pk": column.primary_key,
        })

    return {
        "tableName": model.__tablename__,
        "fields": columns
    }
