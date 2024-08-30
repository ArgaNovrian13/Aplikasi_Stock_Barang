import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:123456@localhost:5432/inventory_db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.getenv('SECRET_KEY')
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwtsecretkey'