from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateUserDto
from api.response import ResponseUserDto
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries


class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        db_employee = user_queries.create_employee(session, request_model)
        session.commit_session()

        response_model = ResponseUserDto(db_employee)

        return await self.make_response_json(body=response_model.dump(), status=201)
