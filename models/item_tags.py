from db import db


class ItemsTags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    tag_id = db.Column(db.Integer, db.ForeingnKey("tag.id"))