from fastapi import FastAPI, Depends

from app.dependencies import get_token_header
from app.internal import admin
from app.routers import banks, users

from fastapi.staticfiles import StaticFiles

from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/app/static", StaticFiles(directory="./app/static"), name="static")

app.include_router(users.router)
app.include_router(banks.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return RedirectResponse('/user/login')
