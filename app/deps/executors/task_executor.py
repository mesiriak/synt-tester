from sqlalchemy import select, update

from app.deps.db import get_session
from app.deps.schemas.task_schema import Task


class TaskExecutor:

    def create_task(self, request):
        session = get_session()
        json = request.get_json()

        new_task = Task(name=json["name"],
                        description=json["description"],
                        status=json["status"],
                        board_id=json["board_id"])

        session.add(new_task)
        session.commit()

        return "Task created with id " + str(new_task.id) + " and name - " + str(new_task.name)

    def get_all_tasks(self):
        session = get_session()
        tasks = session.execute(select(Task)).scalars().all()

        response = {"task " + str(i+1): tasks[i].get_info() for i in range(len(tasks))}

        return response


    def filter_tasks_by_status(self, status):
        session = get_session()
        fetched_boards = session.execute(select(Task).filter(Task.status == status)).scalars().all()

        response = [fetched_boards[i].get_info() for i in range(len(fetched_boards))]

        return response

    def filter_tasks_by_board(self, board_id):
        session = get_session()
        fetched_boards = session.execute(select(Task).filter(Task.board_id == board_id)).scalars().all()

        response = [fetched_boards[i].get_info() for i in range(len(fetched_boards))]

        return response

    def get_task_by_id(self, task_id):
        session = get_session()
        task = session.get(Task, task_id)

        return task.get_info()

    def set_task_status(self, request, task_id):
        session = get_session()
        json = request.get_json()

        stmt = update(Task).where(Task.id == task_id).values(status=bool(json["status"]))

        session.execute(stmt)
        session.commit()

        updated_task = session.get(Task, task_id)

        return updated_task.get_info()

    def delete_task(self, task_id):
        session = get_session()

        deleted_task = session.get(Task, task_id)

        session.delete(deleted_task)
        session.commit()

        return deleted_task.get_info()


