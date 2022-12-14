from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import relationship


from ..db import DBase


class Task(DBase):

    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True)

    name = Column(String)
    description = Column(Text)
    status = Column(Boolean)

    board_id = Column(BigInteger, ForeignKey("boards.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_info(self):
        return "Task with id - " + str(self.id)
