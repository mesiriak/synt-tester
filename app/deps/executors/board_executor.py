from sqlalchemy import select

from app.deps.db import get_session
from app.deps.schemas.board_schema import Board


class BoardExecutor:

    def create_board(self, request):
        session = get_session()

        json = request.get_json()
        new_board = Board(is_open=bool(json["is_open"]))

        session.add(new_board)
        session.commit()

        response = {"board": "id " + str(new_board.id), "objs": new_board.tasks}

        return response

    def get_all_boards(self):
        session = get_session()
        fetched_boards = session.execute(select(Board)).scalars().all()

        response = {"board " + str(i+1): fetched_boards[i].get_info() for i in range(len(fetched_boards))}

        return response
