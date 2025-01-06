from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.http.some_router import some_router

root_router = APIRouter()


@root_router.get("/", tags=["General"])
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="docs/")


root_sub_routers = (some_router,)

for router in root_sub_routers:
    root_router.include_router(router)
