import json
import os

from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    request,
    url_for
)

from app import app
from helper import (
    aws as aws_helper,
    base as base_helper,
    email as email_helper
)
from log_config.custom_logger import logger


mod_home = Blueprint('home', __name__, url_prefix='')


@mod_home.route("/", methods=["GET"])
def index():
    logger.info(f"{__name__}")
    return render_template(
        "index.html"
    )

@mod_home.route("/ping", methods=["GET"])
def ping():
    return {"status": "OK"}
