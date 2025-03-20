from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.db.database import db

class User(db.Model):
    __tablename__ = "user_account"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, nullable=False)
    password: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
    username: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email