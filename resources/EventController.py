from flask import request, jsonify
from flask_restful import Resource
from models.Event import db, Event, EventPostSchema, EventUpdateSchema
import datetime

now = datetime.datetime.now()
events_schema = EventPostSchema(many=True)
event_schema = EventPostSchema()
event_update_schema = EventUpdateSchema()

class GetEvents(Resource):
	def get(self):
		events = Event.query.order_by(db.desc('id')).filter(Event.deleted_at == None).all()

		events = events_schema.dump(events).data
		return {'response':200, 'status': 'success', 'result': events}, 200

class PostEvent(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		# Validate and deserialize input
		data, errors = event_schema.load(json_data)
		if errors:
			return errors, 422

		# Checking data duplicate
		# event = Event.query.filter_by(name=data['name']).first()
		# if category:
		# 	return {'message': 'Event already exists'}, 400

		event = Event(
			user_id=json_data['user_id'],
			description=json_data['description'],
			longitude=json_data['longitude'],
			latitude=json_data['latitude'],
			location=json_data['location'],
			image=json_data['image'],
			created_at=now.strftime("%Y-%m-%d %H:%M:%S"),
			updated_at=now.strftime("%Y-%m-%d %H:%M:%S"),
			deleted_at=None
		)

		db.session.add(event)
		db.session.commit()

		result = event_schema.dump(event).data

		return { "status": 'success', 'data': result }, 201

class UpdateEvent(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		# Validate and deserialize input
		data, errors = event_update_schema.load(json_data)
		if errors:
			return errors, 422

		# Checking data in db
		event = Event.query.filter_by(id=data['id']).first()
		if not event:
			return {'message': 'Event does not exist'}, 400

		event.user_id = data['user_id']
		event.description = data['description']
		event.longitude = data['longitude']
		event.latitude = data['latitude']
		event.location = data['location']
		event.image = data['image']
		event.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
		db.session.commit()

		result = event_schema.dump(event).data

		return { "status": 'success', 'data': result }, 201

class DeleteEvent(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		# Validate and deserialize input
		data, errors = event_update_schema.load(json_data)
		if errors:
			return errors, 422

		# Checking data in db
		event = Event.query.filter_by(id=data['id']).first()
		if not event:
			return {'message': 'Event does not exist'}, 400

		event.deleted_at = now.strftime("%Y-%m-%d %H:%M:%S")
		db.session.commit()

		result = event_schema.dump(event).data

		return { "status": 'success', 'data': result }, 201

class RestoreEvent(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		# Validate and deserialize input
		data, errors = event_update_schema.load(json_data)
		if errors:
			return errors, 422

		# Checking data in db
		event = Event.query.filter_by(id=data['id']).first()
		if not event:
			return {'message': 'Event does not exist'}, 400

		event.deleted_at = None
		db.session.commit()

		result = event_schema.dump(event).data

		return { "status": 'success', 'data': result }, 201

class ForceDeleteEvent(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		# Validate and deserialize input
		data, errors = event_update_schema.load(json_data)
		if errors:
			return errors, 422

		# Checking data in db
		event = Event.query.filter_by(id=data['id']).first()
		if not event:
			return {'message': 'Event does not exist'}, 400

		delete = Event.query.filter_by(id=data['id']).delete()
		db.session.commit()

		return { "status": 'success', 'data': 'deleted' }, 201