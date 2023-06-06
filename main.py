import uvicorn

from users_edit_api.routes import app


if __name__ == "__main__":
    uvicorn.run(app)