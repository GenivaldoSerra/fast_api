from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(
        username='Teste01', email='teste01@teste.com', password='123456'
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste01@teste.com')
    )
    assert result.email == 'teste01@teste.com'
