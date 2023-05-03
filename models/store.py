from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # define in schema.py used Nested
    # items = fields.List(fields.Nested(PlainStoreSchema(), dump_only=True))
    # The cascade parameter is used to specify cascading operations on related
    # child objects when certain operations are performed.
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete"
    )
    # back_populates is a parameter that allows you to specify the other side of
    # a bidirectional relationship between two tables.
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
