from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, status

from app.logic.interactor import Interactor, Request, Response

answer_router = APIRouter()


@answer_router.get("/", status_code=status.HTTP_200_OK)
@inject
async def answer(
    interactor: FromDishka[Interactor], request_data: Annotated[Request, Depends()]
) -> Response:
    return await interactor(request_data=request_data)
