from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.BigInteger, primary_key=True)
	name = db.Column(db.String(255), unique=False, nullable=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), unique=False, nullable=False)
	remember_token = db.Column(db.String(255), unique=False, nullable=False)
	is_activated = db.Column(db.Boolean, unique=False, nullable=False)
	created_at = db.Column(db.TIMESTAMP)
	updated_at = db.Column(db.TIMESTAMP)

	def __init__(self, name, email, username, password, remember_token, is_activated, created_at, updated_at):
		self.name = name
		self.email = email
		self.username = username
		self.password = password
		self.remember_token = remember_token
		self.is_activated = is_activated
		self.created_at = created_at
		self.updated_at = updated_at


class UserSchema(ma.Schema):
	id = fields.Integer()
	name = fields.String(required=True)
	email = fields.String(required=True)
	username = fields.String(required=True)
	password = fields.String(required=True)
	remember_token = fields.String(required=True)
	is_activated = fields.String(required=True)
	created_at = fields.String(required=True)
	updated_at = fields.String(required=True)
