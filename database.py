from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import psycopg2

# Ensure psycopg2-binary is being used
engine = create_engine("postgresql+psycopg2://postgres:22bce1313@localhost/emails")
Base = declarative_base()

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email_from = Column(String(50), nullable=False)
    email_subject = Column(String(60), nullable=False)
    from_date = Column(String(50), nullable=True)
    to_date = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()