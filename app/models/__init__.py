from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def config_db(app):
	db.init_app(app)
	app.db = db
	migrate.init_app(app,app.db)


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(600))
  created_at = db.Column(db.DateTime)
  
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = self.generate_hash(password)
    self.created_at = datetime.now()

  def generate_hash(self, password):
    return generate_password_hash(password)

  def check_hash(self, password):
    return check_password_hash(self.password, password)

  def __repr__(self):
    return '<User %r>' % self.username

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))