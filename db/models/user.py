from sqlalchemy import Column, VARCHAR

from db.models import BaseModel


class DBUser(BaseModel):
    __tablename__ = "users"

    login = Column(VARCHAR(50), unique=True)
    password = Column(VARCHAR(30))
    first_name = Column(VARCHAR(75))
    last_name = Column(VARCHAR(75))