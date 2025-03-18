from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import mysql.connector

db = SQLAlchemy()

def init_db(app: Flask) -> None:
  """Initialize db"""
  db.init_app(app)

def create_database(databaseConfig: Config) -> None:
  """Create database"""
  connection = mysql.connector.connect(
      host=databaseConfig['DB_HOST'],
      user=databaseConfig['DB_USER'],
      password=databaseConfig['DB_PASSWORD']
  )
  cursor = connection.cursor()
  cursor.execute(f"CREATE DATABASE IF NOT EXISTS {databaseConfig['DB_NAME']}")
  cursor.close()
  connection.close()
  connection.close()
