from dishka import Provider, Scope, provide

from app.logic.interactor import Interactor


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    interactor = provide(Interactor)
