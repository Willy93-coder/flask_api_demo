from app.db.database import db
from app.domain.user import User
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(email: str, password: str) -> None | str:
    if _get_user_by_email(email):
        return "User already exists"
    hashed_pw = _hash_password(password)
    user = User(email=email, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

def login_user(email: str, password: str) -> User | str:
    hashed_pw = _hash_password(password)
    user = _get_user_by_email(email)
    if not user or not check_password_hash(user.password, hashed_pw):
        return "Invalid credentials"
    return user

def _hash_password(password: str) -> str:
    hashed_pw = generate_password_hash(password)
    return hashed_pw

def _get_user_by_email(email: str) -> User | None:
    user = db.session.query(User).filter(User.email == email).first()
    return user
