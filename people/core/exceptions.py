class BaseException(Exception):
    message = "Internal Server Error"

    def __init__(self, mensagem: str | None = None) -> None:
        self.message = mensagem if mensagem else self.message


class NotFoundException(BaseException):
    message = "Não encontrado"


class ValueErrorException(BaseException):
    message = "campo VALOR com erros de validação"
