from datetime import datetime
from uuid import UUID
from bson import Decimal128
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from people.database.mongo import db_client
from people.models.jogador import JogadorModel
from people.schemas.jogador import (
    JogadorIn,
    JogadorOut,
    JogadorUpdate,
    JogadorUpdateOut,
)
from people.core.exceptions import NotFoundException, ValueErrorException


class JogadorCdu:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get_client()
        self.db: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.db.get_collection("jogadores")

    async def create(self, body: JogadorIn) -> JogadorOut:
        jogador = JogadorModel(**body.model_dump())
        valor_rep = await self.collection.find_one(
            filter={"valor": Decimal128(body.valor)}
        )
        if float(body.valor) > 200 or float(body.valor) < 15:
            raise ValueErrorException("Campo VALOR fora dos limites!")
        if valor_rep:
            raise ValueErrorException("Campo VALOR repetido!")
        await self.collection.insert_one(jogador.model_dump())
        return JogadorOut(**jogador.model_dump())

    async def get(self, id: UUID) -> JogadorOut:
        jogador = await self.collection.find_one({"id": id})
        if not jogador:
            raise NotFoundException(mensagem=f"Jogador não encontrado com o id: {id}")
        return JogadorOut(**jogador)

    async def get_all(self) -> list[JogadorOut]:
        return [JogadorOut(**jogador) async for jogador in self.collection.find()]

    async def update(self, id: UUID, body: JogadorUpdate) -> JogadorUpdateOut:
        body.updated_at = datetime.now()
        up = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        if not up:
            raise NotFoundException(mensagem=f"Jogador não encontrado com o id: {id}")
        return JogadorUpdateOut(**up)

    async def delete(self, id: UUID) -> None:
        jogador = await self.collection.find_one(filter={"id": id})
        if not jogador:
            raise NotFoundException(mensagem=f"Jogador não encontrado com o id: {id}")
        jogador = await self.collection.delete_one(filter={"id": id})
        return jogador.deleted_count > 0


cdu = JogadorCdu()
