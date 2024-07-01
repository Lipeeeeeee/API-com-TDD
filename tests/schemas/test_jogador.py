from pydantic import ValidationError
import pytest
from people.schemas.jogador import JogadorIn
from tests.jogador_ex import jogador


def test_validacao_schema():
    jogador_ = JogadorIn(**jogador)

    assert jogador_.nome == "Messi"


def test_erro_schema():
    with pytest.raises(ValidationError) as error:
        JogadorIn(nome="Messi", idade=36, valor=30.0)
    assert error.value.errors() == [
        {
            "type": "missing",
            "loc": ("aposentado",),
            "msg": "Field required",
            "input": {"nome": "Messi", "idade": 36, "valor": 30.0},
            "url": "https://errors.pydantic.dev/2.7/v/missing",
        }
    ]
