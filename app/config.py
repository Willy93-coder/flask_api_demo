import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  """Basic configuration for all environments"""

  """Development configuration"""
  DB = os.environ.get('DB')
  DB_DRIVER = os.environ.get('DB_DRIVER')
  DB_USER = os.environ.get('DB_USER')
  DB_PASSWORD = os.environ.get('DB_PASSWORD')
  DB_HOST = os.environ.get('DB_HOST')
  DB_NAME = os.environ.get('DB_NAME')

  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = f'{DB}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
  """Development configuration"""
  DEBUG = True
  

class TestingConfig(Config):
  """Testing configuration"""
  TESTING = True

class ProductionConfig(Config):
  """Production configuration"""
  DEBUG = False

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig
}