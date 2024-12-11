from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import *
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column()
    role_id:Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=True)
    roles = relationship("Role", uselist=False, back_populates="user")

class Role(Base):
    __tablename__ = "roles"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column()
    user = relationship("User", back_populates="roles")
