from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]


class Stage(BaseModel):
    title: str
    date: str
    description: str
    comments: List[str]


class Process(BaseModel):
    date: Optional[str] = None
    skills: Optional[List[str]] = None
    job: Optional[str] = None
    description: Optional[str] = None
    stages: Optional[List[Stage]] = None


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
    applications: Optional[List[Dict[str, Any]]] = None
    processes: Optional[List[Process]] = None

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
                "applications": [
                    {
                        "vacancy": "Software Developer",
                        "status": "Pending",
                        "date_applied": "2024-04-11"
                    },
                    {
                        "vacancy": "Data Scientist",
                        "status": "Accepted",
                        "date_applied": "2024-04-10"
                    }
                ],
                "processes": [
                    {
                        "date": "2024-04-11",
                        "job": "Process Engineer",
                        "skills": ["Skill 1", "Skill 2"],
                        "description": "Description of the process",
                        "stages": [
                            {
                                "title": "Stage 1",
                                "date": "2024-04-11",
                                "description": "Description of stage 1",
                                "comments": []
                            },
                            {
                                "title": "Stage 2",
                                "date": "2024-04-12",
                                "description": "Description of stage 2",
                                "comments": []
                            }
                        ]
                    }
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
    applications: Optional[List[Dict[str, Any]]] = None
    processes: Optional[List[Process]] = None

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
                "applications": [
                    {
                        "vacancy": "Software Developer",
                        "status": "Pending",
                        "date_applied": "2024-04-11"
                    },
                    {
                        "vacancy": "Data Scientist",
                        "status": "Accepted",
                        "date_applied": "2024-04-10"
                    }
                ],
                "processes": [
                    {
                        "date": "2024-04-11",
                        "job": "Process Engineer",
                        "skills": ["Skill 1", "Skill 2"],
                        "description": "Description of the process",
                        "stages": [
                            {
                                "title": "Stage 1",
                                "date": "2024-04-11",
                                "description": "Description of stage 1",
                                "comments": []
                            },
                            {
                                "title": "Stage 2",
                                "date": "2024-04-11",
                                "description": "Description of stage 1",
                                "comments": []
                            }]
                    }]
            }
        })
