from flask import Blueprint, request

from app.deps.executors.task_executor import TaskExecutor

task_router = Blueprint("task", "task_routes")

task_executor = TaskExecutor()


@task_router.get("/")
def task_home():
    return "task"


@task_router.post("/create_task")
def create_task():
    response = task_executor.create_task(request)
    return response
