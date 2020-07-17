from flask_login import current_user
from sqlalchemy import func

from app.mod_auth.models import BaseUser


def get_user(email):
    user_record = BaseUser.query.filter(func.lower(BaseUser.email) == func.lower(email)).first()
    return user_record


