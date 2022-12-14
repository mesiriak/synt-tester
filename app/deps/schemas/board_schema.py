from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime
from sqlalchemy.orm import relationship
from .task_schema import Task

from ..db import DBase


class Board(DBase):

    __tablename__ = "boards"

    id = Column(BigInteger, primary_key=True)

    is_open = Column(Boolean, default=True)

    tasks = relationship("Task", backref="board")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
