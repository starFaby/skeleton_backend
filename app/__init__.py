from flask import Flask
from .config.config import Config
from .database.dataBase import db
from .router.routerUser import user_bp
PORT = 5000
DEBUG = False

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    db.init_app(app)
    return app        

