from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from doc import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    POSTGRES_URL = config.CONFIG['postgresUrl']
    POSTGRES_USER = config.CONFIG['postgresUser']
    POSTGRES_PASS = config.CONFIG['postgresPass']
    POSTGRES_DB = config.CONFIG['postgresDb']
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PASS,
                                                                   url=POSTGRES_URL, db=POSTGRES_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

    db = SQLAlchemy(app)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app