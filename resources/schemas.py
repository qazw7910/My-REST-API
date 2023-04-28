from marshmallow import Schema, fields
# To avoid infinite nesting, we are renaming our schemas which don't use nested fields to Plain,
# such as PlainItemSchema and PlainStoreSchema.

# Then the schemas that do use nesting can be called ItemSchema and StoreSchema, and they inherit
# from the plain schemas. This reduces duplication and prevents infinite nesting.

class PlainItemSchema(Schema):
    # dump_only=True is only included in the serialized dictionary when the object is initially created
    # dump_only in my understanding often used in item create
    # ----------------------------------------------------------------
    # required=True parameter is used to specify that a field is mandatory during deserialization,
    # meaning it must be present when converting a dictionary or JSON object to an object of a certain type.
    # required=True in my understanding it must be present when converting a dictionary or JSON object to an
    # object of a certain type.
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class PlainStoreSchema(Schema):
    # dump_only is only included in the serialized dictionary when the object is initially created
    # dump_only often used in object create
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainStoreSchema(), dump_only=True))
