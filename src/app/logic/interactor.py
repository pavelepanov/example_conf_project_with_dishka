from dataclasses import dataclass

from app.logic.port_and_adapter import Dependency, Port


@dataclass(frozen=True, slots=True)
class Request:
    id: int


@dataclass(frozen=True, slots=True)
class Response:
    my_string: str
    dependency: str
    answer: str


class Interactor:
    def __init__(
        self,
        dependency: Dependency,
        port: Port,
    ):
        self._dependency = dependency
        self._port = port

    async def __call__(self, request_data: Request) -> Response:
        my_string = "Interactor"
        dependency = self._dependency.some_string
        answer = self._port.method()

        return Response(my_string=my_string, dependency=dependency, answer=answer)
