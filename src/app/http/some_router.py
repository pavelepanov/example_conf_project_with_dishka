from fastapi import APIRouter

from app.http.answer import answer_router

some_router = APIRouter(prefix="/some", tags=["Some"])

some_sub_routers = (answer_router,)

for router in some_sub_routers:
    some_router.include_router(router)
