from flask import Blueprint, request

from app.deps.db import get_session
from app.deps.executors.board_executor import BoardExecutor

board_router = Blueprint("board", "board_routes")

board_executor = BoardExecutor()


@board_router.get("/get_board/<int:board_id>")
def board_home(board_id: int):
    return {"board_id": board_id}


@board_router.get("/get_all_boards")
def get_all_boards():
    response = board_executor.get_all_boards()
    return response


@board_router.post("/create_board")
def create_board():
    response = board_executor.create_board(request)
    return response
