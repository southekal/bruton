import os
from flask import (
    Flask,
    render_template,
    request
)
# from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFError, CSRFProtect

from config import Config
from log_config.custom_logger import logger

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', Config))
csrf = CSRFProtect(app)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# jwt = JWTManager(app)


@app.errorhandler(404)
def not_found(error):
    logger.warning(f'page not found {error} - {request.url}')
    return render_template('error_pages/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    logger.error(f'server error {error} - {request.url}')
    return render_template('error_pages/500.html'), 500


# from app.api.auth.controller import api_auth
from app.mod_auth.controller import mod_auth as auth_module
from app.mod_home.controller import mod_home as home_module

# app.register_blueprint(api_auth)
app.register_blueprint(auth_module)
app.register_blueprint(home_module)

# csrf.exempt(api_auth)

