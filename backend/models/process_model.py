from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class Stage(BaseModel):
    title: str
    date: str
    description: str
    comments: List[str]


class Process(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    date: Optional[str] = None
    job: Optional[str] = None
    skills: Optional[str] = None
    description: Optional[str] = None
    stages: Optional[List[Dict[str, Any]]] = None

    model_config = ConfigDict(
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "634a1f89b4781887008b8a00",
                "date": "2024-04-10",
                "job": "Software Developer",
                "skills": "Python, JavaScript, SQL",
                "description": "Recruitment process for software developer position",
                "stages": [
                    {
                        "title": "Initial Screening",
                        "date": "2024-04-10",
                        "description": "Reviewing resumes and conducting initial phone interviews",
                        "comments": ["Shortlisted candidates for next round"]
                    },
                    {
                        "title": "Technical Assessment",
                        "date": "2024-04-15",
                        "description": "Candidates complete coding test",
                        "comments": ["Assessment results pending"]
                    }
                ]
            }
        }
    )


class UpdateProcess(BaseModel):
    date: Optional[str] = None
    job: Optional[str] = None
    skills: Optional[str] = None
    description: Optional[str] = None
    stages: Optional[List[Dict[str, Any]]] = None

    model_config = ConfigDict(
        populate_by_alias=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "date": "2024-04-10",
                "job": "Software Developer",
                "skills": "Python, JavaScript, SQL",
                "description": "Recruitment process for software developer position",
                "stages": [
                    {
                        "title": "Initial Screening",
                        "date": "2024-04-10",
                        "description": "Reviewing resumes and conducting initial phone interviews",
                        "comments": ["Shortlisted candidates for next round"]
                    },
                    {
                        "title": "Technical Assessment",
                        "date": "2024-04-15",
                        "description": "Candidates complete coding test",
                        "comments": ["Assessment results pending"]
                    }
                ]
            }
        }
    )
