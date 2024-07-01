import pytest
from tests.jogador_ex import jogador, jogador_erro
from fastapi import status


async def test_controller_create_sucesso(cliente, url):
    response = await cliente.post(url, json=jogador)
    assert response.status_code == status.HTTP_201_CREATED


async def test_controller_create_erro(cliente, url):
    response = await cliente.post(url, json=jogador_erro)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_controller_get_sucesso(cliente, url, jogador_exists):
    response = await cliente.get(f"{url}{jogador_exists.id}")
    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_erro(cliente, url):
    response = await cliente.get(f"{url}d0cf57b6-001a-4454-af7d-c624bb2ccceb")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.usefixtures("jogadores_exists")
async def test_controller_get_many_sucesso(cliente, url):
    response = await cliente.get(url)
    assert response.status_code == status.HTTP_200_OK


async def test_controller_update_sucesso(cliente, url, jogador_exists):
    response = await cliente.patch(f"{url}{jogador_exists.id}", json={"valor": "50.0"})
    assert response.status_code == status.HTTP_200_OK


async def test_controller_delete_sucesso(cliente, url, jogador_exists):
    response = await cliente.delete(f"{url}{jogador_exists.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
