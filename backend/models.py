from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    genero: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    vacante: Optional[str] = None
    etapas_vancante: Optional[int] = None
    metodo: Optional[str] = None
    etapas_aprobadas: Optional[int] = None
    total_feedback: Optional[int] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "634a1f89b4781887008b8a00",  # Example of a valid ObjectId string
                "nombre": "Juan Perez",
                "apellido": "Rodriguez",
                "genero": "Masculino",
                "email": "juan.perez@example.com",
                "telefono": "+521 5512345678",
                "vacante": "Desarrollador Python",
                "etapas_vancante": 3,
                "metodo": "Aplicacion en linea",
                "etapas_aprobadas": 2,
                "total_feedback": 1,
            }
        },
    )


class UpdateUser(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    genero: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    vacante: Optional[str] = None
    etapas_vancante: Optional[int] = None
    metodo: Optional[str] = None
    etapas_aprobadas: Optional[int] = None
    total_feedback: Optional[int] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "nombre": "Juan Perez",
                "apellido": "Rodriguez",
                "genero": "Masculino",
                "email": "juan.perez@example.com",
                "telefono": "+521 5512345678",
                "vacante": "Desarrollador Python",
                "etapas_vancante": 3,
                "metodo": "Aplicacion en linea",
                "etapas_aprobadas": 2,
                "total_feedback": 1,
            }
        },
    )
