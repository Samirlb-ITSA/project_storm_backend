from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
import uuid

class HistoryStatus(Base):
    __tablename__ = "history_status"

    statusid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)

    # Define the relationship with JobOfferHistory
    job_offer_histories = relationship("JobOfferHistory", back_populates="status")


class HistoryStatusIn(BaseModel):
    statusid: str
    name: str