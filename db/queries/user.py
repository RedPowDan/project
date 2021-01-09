from api.request import RequestCreateEmployeeDto
from db.database import DBSession
from db.models import DBUser


def create_user(session: DBSession, user: RequestCreateEmployeeDto) -> DBUser:
    new_user = DBUser(
        login=user.login,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    session.add_model(new_user)

    return new_user
