from models.database import db
import json
import uuid

class Avenger(db.Model):
    __tablename__ = 'avengers'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  
    name = db.Column(db.String(100), nullable=False)        
    alias = db.Column(db.String(100), nullable=False)       
    abilities = db.Column(db.Text, nullable=False)          
    actor = db.Column(db.String(100), nullable=False)       
    def __repr__(self):
        return f"<Avenger {self.alias} ({self.name})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "alias": self.alias,
            "abilities": json.loads(self.abilities),
            "actor": self.actor
        }
