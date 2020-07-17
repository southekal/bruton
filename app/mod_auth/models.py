from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import (
    ARRAY,
    JSONB
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from app import (
    db,
    login
)


@login.user_loader
def load_user(id):
    return BaseUser.query.get(int(id))


class BaseUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    org = db.Column(db.String(240), index=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, unique=False, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
