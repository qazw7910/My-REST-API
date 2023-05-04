from marshmallow import Schema, fields


# To avoid infinite nesting, we are renaming our schemas which don't use nested fields to Plain,
# such as PlainItemSchema and PlainStoreSchema.
# ----------------------------------------------------------------
# Then the schemas that do use nesting can be called ItemSchema and StoreSchema, and they inherit
# from the plain schemas. This reduces duplication and prevents infinite nesting.
# ----------------------------------------------------------------
# Deserialization is the process of converting data that has been serialized (i.e.,
# transformed into a format that can be stored or transmitted) back into its original
# form so that it can be used in an application.

# ----------------------------------------------------------------
# Same Layer
class PlainItemSchema(Schema):
    # dump_only=True n the context of APIs, deserialization is often used to convert data received from a
    # request (e.g., JSON data in the request body) into Python objects that can be processed by the API.
    # dump_only=True is a parameter in the marshmallow library, which is used to specify that the field is
    # only included when serializing (that is, converting the object to JSON or other formats)
    # ----------------------------------------------------------------
    # required=True parameter is used to specify that a field is mandatory during deserialization,
    # meaning it must be present when converting a dictionary or JSON object to an object of a certain type.
    # required=True in my understanding it must be present when converting a dictionary or JSON object to an
    # object of a certain type.
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    # dump_only is only included in the serialized dictionary when the object is initially created
    # dump_only often used in object create
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


# ----------------------------------------------------------------
# Same Layer Plain__Schema
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
# ----------------------------------------------------------------
# secondary Table
class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema())
    tag = fields.Nested(TagSchema())
