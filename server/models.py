from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    # This will make sure only actual fields are serialized
    serialize_rules = ('-__dict__', '-_sa_instance_state')

    def update(self, data: dict):
        # Update only attributes that exist on this model
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'
