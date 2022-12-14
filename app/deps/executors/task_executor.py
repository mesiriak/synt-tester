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
