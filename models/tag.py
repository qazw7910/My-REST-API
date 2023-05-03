from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    # back_populates is a parameter that allows you to specify the other side of
    # a bidirectional relationship between two tables.
    store = db.relationship("StoreModel", back_populates="tags")