from main import db
from datetime import datetime

class Board(db.Model):

    id = db.Column(db.Integer, primary_key=True)


    is_open = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
