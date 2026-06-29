from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routers.dynamic_forms_router import router as dynamic_forms_router
from app.routers.cash_flow_router import router as cash_flow_router
from app.routers import auth, forms_router, user_api, dashboard_router, approvals, month_router
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cash_flow_router)
app.include_router(dynamic_forms_router)
app.include_router(month_router.router)
app.include_router(dashboard_router.router)
app.include_router(forms_router.router)
app.include_router(auth.router)
app.include_router(user_api.router)
app.include_router(approvals.router)



# این دو خط رو با شرط جایگزین کن
if os.path.exists("frontend/dist/assets"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

if os.path.exists("frontend/dist"):
    app.mount("/icons.svg", StaticFiles(directory="frontend/dist"), name="icons")

    @app.get("/{full_path:path}", include_in_schema=False)
    def serve_react(full_path: str):
        return FileResponse("frontend/dist/index.html")
