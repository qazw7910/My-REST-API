from marshmallow import Schema, fields


class ItemSchema(Schema):
    # dump_only=True is only included in the serialized dictionary when the object is initially created
    # dump_only in my understanding often used in item create
    #----------------------------------------------------------------
    # required=True parameter is used to specify that a field is mandatory during deserialization,
    # meaning it must be present when converting a dictionary or JSON object to an object of a certain type.
    # required=True in my understanding it must be present when converting a dictionary or JSON object to an
    # object of a certain type.
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    # dump_only is only included in the serialized dictionary when the object is initially created
    # dump_only often used in item create
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
