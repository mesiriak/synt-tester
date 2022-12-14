from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import relationship


from ..db import DBase


class Task(DBase):

    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True)

    name = Column(String)
    description = Column(Text)
    status = Column(Boolean, default=False)

    board_id = Column(BigInteger, ForeignKey("boards.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_info(self):

        info = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "board_id": self.board_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

        return info
