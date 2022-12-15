from flask import Blueprint, request

from app.deps.executors.task_executor import TaskExecutor

task_router = Blueprint("task", "task_routes")

task_executor = TaskExecutor()


@task_router.get("/")
def task_home():
    return "task"


@task_router.get("/get_all_tasks")
def get_all_tasks():
    response = task_executor.get_all_tasks()
    return response

@task_router.get("/get_task_by_id/<int:task_id>")
def get_task_by_id(task_id: int):
    response = task_executor.get_task_by_id(task_id)
    return response

@task_router.get("/filter_tasks_by_status/<int:status>")
def filter_tasks_by_status(status: int):
    response = task_executor.filter_tasks_by_status(bool(status))
    return response


@task_router.get("/filter_tasks_by_board/<int:board_id>")
def filter_tasks_by_board(board_id: int):
    response = task_executor.filter_tasks_by_board(board_id)
    return response

@task_router.post("/create_task")
def create_task():
    response = task_executor.create_task(request)
    return response

@task_router.patch("/set_task_status/<int:task_id>")
def set_task_status(task_id: int):
    response = task_executor.set_task_status(request, task_id)
    return response


@task_router.delete("/delete_task/<int:task_id>")
def delete_task(task_id: int):
    response = task_executor.delete_task(task_id)
    return response
