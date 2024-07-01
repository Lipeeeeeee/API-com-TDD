from motor.motor_asyncio import AsyncIOMotorClient
from people.core.config import configs


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(configs.URL_BD)

    def get_client(self) -> AsyncIOMotorClient:
        return self.client


db_client = MongoClient()
