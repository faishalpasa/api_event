from flask import Blueprint
from flask_restful import Api
from resources.EventController import GetEvents, PostEvent, UpdateEvent, DeleteEvent, ForceDeleteEvent, RestoreEvent

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(GetEvents, '/events')
api.add_resource(PostEvent, '/events/post')
api.add_resource(UpdateEvent, '/events/update')
api.add_resource(DeleteEvent, '/events/delete')
api.add_resource(RestoreEvent, '/events/restore')
api.add_resource(ForceDeleteEvent, '/events/force_delete')