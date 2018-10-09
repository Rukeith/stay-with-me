from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:pass@127.0.0.1:3400/demo'
    )
    db.init_app(app)

    from flaskr.routes.demo import api_blueprint as demo_blueprint
    app.register_blueprint(demo_blueprint)
    return app