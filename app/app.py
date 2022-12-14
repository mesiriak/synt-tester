from flask import Flask
from .deps.db import init_db
from .routers.board_router import board_router
from .routers.task_router import task_router


def create_app() -> Flask:
    init_db()

    app = Flask("Synthetic")
    app.register_blueprint(board_router, url_prefix="/board")
    app.register_blueprint(task_router, url_prefix="/task")

    return app

