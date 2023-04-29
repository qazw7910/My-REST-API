from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from db import db

from models import StoreModel
from resources.schemas import StoreSchema



blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("Deleting an Item is not implemented.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400, message="A store with the same name already exists"
            )
        except SQLAlchemyError:
            abort(
                500, message="An error occurred creating the store"
            )

        return store
