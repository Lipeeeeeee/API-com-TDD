from datetime import datetime
from decimal import Decimal
from typing import Any
import uuid
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_serializer


class BaseClass(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self_value = dict(self)
        for key, value in self_value.items():
            if isinstance(value, Decimal):
                self_value[key] = Decimal128(str(value))
        return self_value
