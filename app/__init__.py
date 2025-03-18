from flask import Flask
from .config import config
from .db.database import db, init_db, create_database
from flask_migrate import Migrate

migrate = Migrate()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    create_database(app.config)

    init_db(app)
    migrate.init_app(app, db)

    return app