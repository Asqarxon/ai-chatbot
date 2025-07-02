# backend/models.py

"""
This module is reserved for ORM or data models.
You can define SQLAlchemy models or shared Pydantic schemas here.
"""

# Example structure (uncomment and modify when needed):

# from sqlalchemy import Column, Integer, String, Text, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime

# Base = declarative_base()

# class Conversation(Base):
#     __tablename__ = "conversations"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, nullable=False)
#     username = Column(String(255))
#     user_message = Column(Text, nullable=False)
#     ai_response = Column(Text, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
