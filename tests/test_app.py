from http import HTTPStatus

from fast_api.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olar mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testeusername',
        'email': 'teste@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'testeuser',
            'email': 'teste1@test.com',
            'password': 'password1',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'testeuser',
        'email': 'teste1@test.com',
    }


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.json() == {'users': [user_schema]}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'Usuário deletado!'}
