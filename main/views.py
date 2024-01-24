from fastapi import Request, Response
from main import main
import time
from main.database.models import query_execute, Users


@main.middleware("http")
async def before_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@main.get("/api/add_user")
async def api_add_user(name: str, gender: str):

    await query_execute(
        query_text=f'insert into users (name, gender) values (\'{name}\', \'{gender}\')',
        fetch_all=False,
        type_query='insert'
    )

    return {'message': "OK"}


@main.get("/")
async def index():
    users: [Users] = await query_execute(query_text='select * from users', fetch_all=True, type_query='read')
    return {'message': "OK", 'data': [{'name': i.name, 'gender': i.gender} for i in users]}
