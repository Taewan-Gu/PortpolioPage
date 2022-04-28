from sqlalchemy import JSON, BigInteger, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class TimeBase:
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, onupdate=func.now())
