from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: Optional[str] = None
    cellphone: Optional[str] = None
    birthday: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    professionalProfile: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    linkProfilePhoto: Optional[str] = None
    typeProfile: Optional[str] = None
    processes: Optional[List[str]] = None

    model_config = ConfigDict(
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "634a1f89b4781887008b8a00",
                "name": "John Doe",
                "cellphone": "+521 5512345678",
                "birthday": "1990-01-01",
                "gender": "Male",
                "email": "john.doe@example.com",
                "password": "password123",
                "professionalProfile": "Software Engineer",
                "address": "123 Main St",
                "city": "Anytown",
                "state": "Anystate",
                "postalCode": "12345",
                "linkProfilePhoto": "http://example.com/profile.jpg",
                "typeProfile": "Type A",
                "processes": [
                    "634a1f89b4781887008b8a00",
                ]
            }
        },
    )


class UpdateUser(BaseModel):
    name: Optional[str] = None
    cellphone: Optional[str] = None
    birthday: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    professionalProfile: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    linkProfilePhoto: Optional[str] = None
    typeProfile: Optional[str] = None
    processes: Optional[List[str]] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "cellphone": "+521 5512345678",
                "birthday": "1990-01-01",
                "gender": "Male",
                "email": "john.doe@example.com",
                "password": "password123",
                "professionalProfile": "Software Engineer",
                "address": "123 Main St",
                "city": "Anytown",
                "state": "Anystate",
                "postalCode": "12345",
                "linkProfilePhoto": "http://example.com/profile.jpg",
                "typeProfile": "Type A",
                "processes": ["634a1f89b4781887008b8a00",]
            }
        })


class UpdateUserProcesses(BaseModel):
    processes: Optional[List[str]] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "processes": ["634a1f89b4781887008b8a00",],
            }
        })
