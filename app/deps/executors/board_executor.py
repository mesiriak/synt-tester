from sqlalchemy import select

from app.deps.db import get_session
from app.deps.schemas.board_schema import Board


class BoardExecutor:

    def create_board(self, request):
        session = get_session()
        new_board = Board(is_open=request.args.get("is_open"))

        session.add(new_board)
        session.commit()

        return {"response": "board created with id " + str(new_board.id), "objs": new_board.tasks}

    def get_board_tasks(self, board_id):
        session = get_session()
        board = session.get(Board, board_id)

        response = {"task " + str(i+1): board.tasks[i].get_info() for i in range(len(board.tasks))}

        return response

    def get_all_boards(self):
        session = get_session()

        fetched_boards = session.execute(select(Board)).scalars().all()

        response = {"board " + str(i+1): fetched_boards[i].get_info() for i in range(len(fetched_boards))}

        return response
