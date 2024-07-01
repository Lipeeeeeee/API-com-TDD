from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, Field
from people.schemas.base import BaseSchema, ConvertionOut


class JogadorBase(BaseSchema):
    nome: str = Field(description="Nome do jogador")
    idade: int = Field(description="idade do jogador")
    valor: Decimal = Field(description="valor de mercado do jogador")
    aposentado: bool = Field(description="é aposentado ou não")


class JogadorIn(JogadorBase):
    pass


class JogadorOut(ConvertionOut, JogadorIn):
    pass


def convert_decimal(value):
    return Decimal128(str(value))


decimal_ = Annotated[Decimal, AfterValidator(convert_decimal)]


class JogadorUpdate(BaseSchema):
    nome: Optional[str] = Field(None, description="Nome do jogador")
    idade: Optional[int] = Field(None, description="idade do jogador")
    valor: Optional[decimal_] = Field(None, description="valor de mercado do jogador")
    aposentado: Optional[bool] = Field(None, description="é aposentado ou não")
    updated_at: datetime = Field(default_factory=datetime.now)


class JogadorUpdateOut(JogadorOut):
    ...
