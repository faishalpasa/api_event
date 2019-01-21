from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.User import User


ma = Marshmallow()
db = SQLAlchemy()

class Event(db.Model):
	__tablename__ = 'event'
	id = db.Column(db.BigInteger, primary_key=True)
	user_id = db.Column(db.Integer, nullable=False)
	#user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
	#users = db.relationship('User', backref=db.backref('event', lazy='dynamic'))
	description = db.Column(db.Text, unique=False, nullable=True)
	location = db.Column(db.String(255), unique=False, nullable=False)
	longitude = db.Column(db.String(255), unique=False, nullable=False)
	latitude = db.Column(db.String(255), unique=False, nullable=False)
	image = db.Column(db.String(255), unique=False, nullable=False)
	created_at = db.Column(db.TIMESTAMP)
	updated_at = db.Column(db.TIMESTAMP)
	deleted_at = db.Column(db.TIMESTAMP)

	def __init__(self, user_id, description, location, longitude, latitude, image, created_at, updated_at, deleted_at):
		self.user_id = user_id
		self.description = description
		self.location = location
		self.longitude = longitude
		self.latitude = latitude
		self.image = image
		self.created_at = created_at
		self.updated_at = updated_at
		self.deleted_at = deleted_at


class EventPostSchema(ma.Schema):
	id = fields.Integer()
	user_id = fields.Integer(required=True)
	description = fields.String(required=True)
	location = fields.String(required=True)
	longitude = fields.String(required=True)
	latitude = fields.String(required=True)
	image = fields.String(required=True)
	created_at = fields.String(required=True)
	updated_at = fields.String(required=True)
	deleted_at = fields.String(required=False)

class EventUpdateSchema(ma.Schema):
	id = fields.Integer(required=True)
	user_id = fields.Integer(required=True)
	description = fields.String(required=False)
	location = fields.String(required=False)
	longitude = fields.String(required=False)
	latitude = fields.String(required=False)
	image = fields.String(required=False)
	created_at = fields.String(required=False)
	updated_at = fields.String(required=False)
	deleted_at = fields.String(required=False)
