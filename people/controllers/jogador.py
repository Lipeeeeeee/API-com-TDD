from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from pytest import ExceptionInfo

from people.cdu.jogador import JogadorCdu
from people.core.exceptions import NotFoundException, ValueErrorException
from people.schemas.jogador import (
    JogadorIn,
    JogadorOut,
    JogadorUpdate,
    JogadorUpdateOut,
)

router = APIRouter(tags=["jogadores"])


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=JogadorOut,
    summary="Registrar jogador",
)
async def post(body: JogadorIn = Body(...), cdu: JogadorCdu = Depends()) -> JogadorOut:
    try:
        return await cdu.create(body=body)
    except ExceptionInfo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao inserir, preencha os campos corretamente",
        )
    except ValueErrorException as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error.message
        )


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=JogadorOut,
    summary="Recuperar jogador",
)
async def get(id: UUID4 = Path(alias="id"), cdu: JogadorCdu = Depends()) -> JogadorOut:
    try:
        return await cdu.get(id=id)
    except NotFoundException as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=list[JogadorOut],
    summary="Recuperar jogadores",
)
async def get_all(cdu: JogadorCdu = Depends()) -> list[JogadorOut]:
    return await cdu.get_all()


@router.patch(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=JogadorOut,
    summary="Atualizar jogador",
)
async def patch(
    body: JogadorUpdate, id: UUID4 = Path(alias="id"), cdu: JogadorCdu = Depends()
) -> JogadorUpdateOut:
    try:
        return await cdu.update(id=id, body=body)
    except NotFoundException as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


@router.delete(
    path="/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar jogador"
)
async def delete(id: UUID4 = Path(alias="id"), cdu: JogadorCdu = Depends()) -> None:
    try:
        return await cdu.delete(id=id)
    except NotFoundException as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
