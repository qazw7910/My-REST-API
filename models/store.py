from sqlalchemy import delete

from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # define in schema.py used Nested
    # items = fields.List(fields.Nested(PlainStoreSchema(), dump_only=True))
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
