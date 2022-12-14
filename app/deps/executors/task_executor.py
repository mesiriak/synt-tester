from sqlalchemy import select

from app.deps.db import get_session
from app.deps.schemas.task_schema import Task


class TaskExecutor:

    def create_task(self, request):
        session = get_session()
        print(request.form)
        new_task = Task(name=request.args.get("name"),
                        description=request.args.get("description"),
                        board_id=4)

        session.add(new_task)
        session.commit()

        return "Task created with id " + str(new_task.id) + " and name - " + str(new_task.name)

    def get_all_tasks(self):
        session = get_session()
        tasks = session.execute(select(Task)).scalars().all()

        response = {"task " + str(i+1): tasks[i].get_info() for i in range(len(tasks))}

        return response


    def get_tasks_by_status(self, status):
        session = get_session()
        fetched_boards = session.execute(select(Task).filter(Task.status == status)).scalars().all()

        response = [fetched_boards[i].get_info() for i in range(len(fetched_boards))]

        return response

    def get_tasks_by_board(self, board_id):
        session = get_session()
        fetched_boards = session.execute(select(Task).filter(Task.board_id == board_id)).scalars().all()

        response = [fetched_boards[i].get_info() for i in range(len(fetched_boards))]

        return response

    def set_task_status(self, task_id, status):
        session = get_session()
        pass

