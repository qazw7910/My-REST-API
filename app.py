import uuid
from flask import Flask, request
from flask_smorest import abort

from db import stores, items

app = Flask(__name__)


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, "Item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "name" not in item_data or "price" not in item_data:
        abort(404, "bad request. Please ensure 'price' and 'name' are included in the json payload")
    try:
        item = item_data
        items[item_id] |= item

        return item

    except KeyError:
        abort(404, "Item not found")


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )
    for item in items.values():
        if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"Item already exists.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        # Here you might also want to add the items in this store
        # We'll do that later on in the course
        return stores[store_id]
    except KeyError:
        return abort(404, message="Store not found.")


@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400,
              message="Bad request. Ensure 'name' is included in the JSON payload.",
              )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"Store already exists.")

    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found.")


if __name__ == '__main__':
    app.run()
