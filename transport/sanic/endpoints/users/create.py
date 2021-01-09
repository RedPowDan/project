from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateUserDto
from api.response import ResponseUserDto
from db.exceptions import DBIntegrityException
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries


class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        db_user = user_queries.create_user(session, request_model)
        try:
            session.commit_session()
        except DBIntegrityException:
            return await self.make_response_json(body={"Error message": "such a login exists"}, status=409)
        response_model = ResponseUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
