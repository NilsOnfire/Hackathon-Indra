from fastapi import APIRouter, HTTPException
from queries.user_queries import get_one_user_email
from pydantic import BaseModel

auth = APIRouter()


# obtener un usuario por su email
async def get_user_by_email(email):
    user = await get_one_user_email(email)
    return user

# verificar la contraseña (sin hash)


def verify_password_plain(plain_password, stored_password):
    return plain_password == stored_password

# Ruta para la autenticación de usuarios


class UserLogin(BaseModel):
    email: str
    password: str

# Ruta para la autenticación de usuarios


@auth.post("/api/login", tags=["Authentication"])
async def login_for_access_token(user_login: UserLogin):
    user = await get_one_user_email(user_login.email)
    if not user:
        raise HTTPException(
            status_code=401, detail="Incorrect email or password")
    if not verify_password_plain(user_login.password, user["password"]):
        raise HTTPException(
            status_code=401, detail="Incorrect email or password")

    # Obtener el ID del usuario desde MongoDB (_id)
    idUser = str(user["_id"])

    # Retorna el ID del usuario
    return {"idUser": idUser}
