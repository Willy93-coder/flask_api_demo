from __future__ import annotations
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.db.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "user_account"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, nullable=False)
    password: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
    username: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, nullable=True)

    def __init__(self, email: str, password: str, username: str = None):
        self.email = email
        self.password = password
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.email
    
    @staticmethod
    def register_user(email: str, password: str) -> None | str:
        if User._get_user_by_email(email):
            return "User already exists"
        hashed_pw = User._hash_password(password)
        user = User(email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return None

    @staticmethod
    def login_user(email: str, password: str) -> User | None:
        user = User._get_user_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return None
        return user

    def _hash_password(password: str) -> str:
        hashed_pw = generate_password_hash(password)
        return hashed_pw

    def _get_user_by_email(email: str) -> User | None:
        user = db.session.query(User).filter(User.email == email).first()
        return user