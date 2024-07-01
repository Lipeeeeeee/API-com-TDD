import asyncio
from uuid import UUID
import pytest
from people.database.mongo import db_client
from people.schemas.jogador import JogadorIn, JogadorUpdate
from tests.jogador_ex import jogador, jogadores
from people.cdu.jogador import cdu
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def cliente_mongo():
    return db_client.get_client()


@pytest.fixture(autouse=True)
async def clear_db(cliente_mongo):
    yield
    collections = await cliente_mongo.get_database().list_collection_names()
    for collection in collections:
        if not collection.startswith("system"):
            await cliente_mongo.get_database()[collection].delete_many({})


@pytest.fixture
async def cliente() -> AsyncClient:
    from people.main import app

    async with AsyncClient(app=app, base_url="https://test") as client:
        yield client


@pytest.fixture
def url() -> str:
    return "/jogadores/"


@pytest.fixture
def jogador_id() -> UUID:
    return UUID("b6fa7373-f231-4304-aef9-24d8018f6f6d")


@pytest.fixture
def jogador_in(jogador_id):
    return JogadorIn(**jogador, id=jogador_id)


@pytest.fixture
def jogador_up(jogador_id):
    return JogadorUpdate(**jogador, id=jogador_id)


@pytest.fixture
async def jogador_exists(jogador_in):
    return await cdu.create(jogador_in)


@pytest.fixture
def jogadores_in():
    return [JogadorIn(**jogador_) for jogador_ in jogadores]


@pytest.fixture
async def jogadores_exists(jogadores_in):
    return [await cdu.create(body=jogador_) for jogador_ in jogadores_in]
