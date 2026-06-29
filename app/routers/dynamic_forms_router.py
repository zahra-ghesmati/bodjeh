from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from app.services.auth_service import get_current_user

from app.schemas.dynamic_form import SaveDynamicFormRequest

from app.config.dynamic_form_configs import SERVICE_MAP as DYNAMIC_SERVICE_MAP
from app.services.dynamic_form_service import (
    get_rows_dynamic_form,
    save_rows_dynamic_form,
)
from app.services.form_dispatcher import get_form_meta


router = APIRouter(prefix="/forms", tags=["Dynamic Forms"])


def get_dynamic_config_or_404(form_key: str):
    config = DYNAMIC_SERVICE_MAP.get(form_key)

    if not config:
        raise HTTPException(
            status_code=404,
            detail="فرم داینامیک یافت نشد"
        )

    return config


def make_meta_endpoint(form_key: str):
    def endpoint():
        config = get_dynamic_config_or_404(form_key)
        meta = config["meta"].copy()
        meta["type"] = "dynamic"
        meta["columns"] = config["columns"]
        meta["allow_add_rows"] = config.get("allow_add_rows", False)
        meta["approval"] = config.get("approval", {"type": "single"})  # این خط اضافه شه
        return meta
    return endpoint


def make_rows_endpoint(form_key: str):
    def endpoint(
        company: str,
        year: str,
        month: str,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
    ):
        config = get_dynamic_config_or_404(form_key)

        return get_rows_dynamic_form(
            config=config,
            db=db,
            company=company,
            year=year,
            month=month,
            current_user=current_user,
        )

    return endpoint


def make_save_endpoint(form_key: str):
    def endpoint(
        payload: SaveDynamicFormRequest,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
    ):
        config = get_dynamic_config_or_404(form_key)

        return save_rows_dynamic_form(
            config=config,
            db=db,
            payload=payload,
            current_user=current_user,
        )

    return endpoint


for form_key in DYNAMIC_SERVICE_MAP.keys():
    router.add_api_route(
        f"/{form_key}/meta",
        make_meta_endpoint(form_key),
        methods=["GET"],
        name=f"dynamic_{form_key}_meta",
    )

    router.add_api_route(
        f"/{form_key}/rows",
        make_rows_endpoint(form_key),
        methods=["GET"],
        name=f"dynamic_{form_key}_rows",
    )

    router.add_api_route(
        f"/{form_key}/save",
        make_save_endpoint(form_key),
        methods=["POST"],
        name=f"dynamic_{form_key}_save",
    )
