from decimal import Decimal
from uuid import UUID
import pytest
from people.cdu.jogador import cdu
from people.schemas.jogador import JogadorIn, JogadorOut, JogadorUpdateOut
from people.core.exceptions import NotFoundException, ValueErrorException
from tests.jogador_ex import jogador_erro


async def test_cdu_create_sucesso(jogador_in):
    result = await cdu.create(body=jogador_in)

    assert isinstance(result, JogadorOut)
    assert result.idade == 36


async def test_cdu_create_erro():
    with pytest.raises(ValueErrorException) as error:
        await cdu.create(body=JogadorIn(**jogador_erro))
    assert error.value.errors() == [
        {
            "type": "string_type",
            "loc": ("nome",),
            "msg": "Input should be a valid string",
            "input": True,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        }
    ]


async def test_cdu_get_sucesso(jogador_exists):
    result = await cdu.get(id=jogador_exists.id)

    assert isinstance(result, JogadorOut)
    assert result.nome == "Messi"


async def test_cdu_get_erro():
    with pytest.raises(NotFoundException) as error:
        await cdu.get(id=UUID("703e120a-614a-4f40-aa4d-4bf89b12edc6"))
    assert (
        error.value.message
        == "Jogador não encontrado com o id: 703e120a-614a-4f40-aa4d-4bf89b12edc6"
    )


@pytest.mark.usefixtures("jogadores_exists")
async def test_cdu_get_many_sucesso():
    result = await cdu.get_all()

    assert isinstance(result, list)
    assert len(result) > 1


async def test_cdu_update_sucesso(jogador_up, jogador_exists):
    jogador_up.valor = "50.0"
    result = await cdu.update(id=jogador_exists.id, body=jogador_up)

    assert isinstance(result, JogadorUpdateOut)
    assert result.valor == Decimal("50.0")
    assert result.created_at != result.updated_at


async def test_cdu_update_erro(jogador_up):
    with pytest.raises(NotFoundException) as error:
        await cdu.update(
            id=UUID("703e120a-614a-4f40-aa4d-4bf89b12edc6"), body=jogador_up
        )
    assert (
        error.value.message
        == "Jogador não encontrado com o id: 703e120a-614a-4f40-aa4d-4bf89b12edc6"
    )


async def test_cdu_delete_sucesso(jogador_exists):
    result = await cdu.delete(id=jogador_exists.id)

    assert result is True


async def test_cdu_delete_erro():
    with pytest.raises(NotFoundException) as error:
        await cdu.delete(id=UUID("703e120a-614a-4f40-aa4d-4bf89b12edc6"))
    assert (
        error.value.message
        == "Jogador não encontrado com o id: 703e120a-614a-4f40-aa4d-4bf89b12edc6"
    )
