from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:pass@127.0.0.1:3400/shopee24_dev'
    )
    db.init_app(app)
    migrate = Migrate(app, db)

    from flaskr.routes.demo import api_blueprint as demo_blueprint
    app.register_blueprint(demo_blueprint)
    return app