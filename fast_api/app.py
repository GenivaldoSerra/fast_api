from http import HTTPStatus
from fastapi import FastAPI
from fast_api.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olar mundo!'}

@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED )
def create_user(user: UserSchema):
    return user