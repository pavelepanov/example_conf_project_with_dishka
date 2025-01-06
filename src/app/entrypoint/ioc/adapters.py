from dishka import Provider, Scope, from_context, provide

from app.entrypoint.config import Config
from app.logic.port_and_adapter import Adapter, Dependency, Port


class ConfigProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)


class SomeConfigProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_dependency(self, config: Config) -> Dependency:
        return Dependency(some_string=f"Some info + {config.some_config.some_string}")


class AnswerProvider(Provider):
    port = provide(Adapter, scope=Scope.REQUEST, provides=Port)
