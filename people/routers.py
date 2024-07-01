from fastapi import APIRouter
from people.controllers.jogador import router

main_router = APIRouter()
main_router.include_router(router, prefix="/jogadores")
