from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.update(
        FLASK_ENV="development",
        SQLALCHEMY_ECHO=True,
        SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:rukeith@127.0.0.1:5432/stay_with_me'
    )
    # db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes.demo import api_blueprint as demo_blueprint
    from .routes.user import api_blueprint as user_blueprint
    app.register_blueprint(demo_blueprint)
    app.register_blueprint(user_blueprint)
    from .models import User
    with app.app_context():
        print('1---------')
        db.create_all()
        db.session.commit()
        print('2---------')
    return app
