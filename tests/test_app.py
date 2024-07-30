from http import HTTPStatus


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
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testeusername',
                'email': 'teste@test.com',
            }
        ]
    }


def test_update_user(client):
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


def test_read_user_id(client):
    response = client.get('/users/1')

    assert response.json() == {
        'id': 1,
        'username': 'testeuser',
        'email': 'teste1@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'Usuário deletado!'}
