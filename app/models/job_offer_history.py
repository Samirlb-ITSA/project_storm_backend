from sqlalchemy import Column, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class JobOfferHistory(Base):
    __tablename__ = "job_offer_history"

    historyid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    offerid = Column(UUID, ForeignKey('job_offers.offerid'))
    userid = Column(UUID, ForeignKey('users.userid'))
    statusid = Column(UUID, ForeignKey('history_status.statusid'))
    changedate = Column(DateTime, default=datetime.now)

    # Define the relationship with User
    user = relationship("User")

    # Define the relationship with HistoryStatus
    status = relationship("HistoryStatus", back_populates="job_offer_histories")

class JobOfferHistoryIn(BaseModel):
    historyid: str
    offerid: str
    userid: str
    statusid: str
    changedate: datetime