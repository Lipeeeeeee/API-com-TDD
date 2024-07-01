from fastapi import FastAPI
from people.routers import main_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args, **kwargs, version="0.0.1", title="Cadastro de Jogadores de Futebol"
        )


app = App()
app.include_router(main_router)
