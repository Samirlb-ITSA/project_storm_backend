from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from config.db_config import get_db_connection
from models.user_model import User
from models.job_offer_model import JobOffer
from models.applicant_model import Applicant
from models.role_model import Role
from datetime import datetime, timedelta

router = APIRouter()

class StatisticsController:
    def getStatistics(self):
        db = get_db_connection()
        non_admin_users = db.query(User).join(User.roles).filter(Role.name != 'admin').all()

        # Initialize the statistics
        stats = {
            "total_job_offers": 0,
            "job_offers_per_user": {},
            "success_rate": {},
            "total_users": 0,
            "new_users_percentage_last_month": 0,
        }

        # Calculate the statistics
        for user in non_admin_users:
            # Count the number of job offers for each user
            job_offers_count = db.query(Applicant).filter(Applicant.userid == user.userid).count()
            stats["job_offers_per_user"][user.email] = job_offers_count

            # Count the number of successful job offers for each user
            successful_job_offers_count = db.query(Applicant).join(JobOffer, Applicant.offerid == JobOffer.offerid).filter(Applicant.userid == user.userid, JobOffer.status == 1).count()
            stats["success_rate"][user.email] = successful_job_offers_count / job_offers_count if job_offers_count > 0 else 0

        # Count the total number of job offers
        stats["total_job_offers"] = db.query(JobOffer).count()

        # Count the total number of users
        stats["total_users"] = db.query(User).count()

        # Count the total number of users registered in the last month
        one_month_ago = datetime.now() - timedelta(days=30)
        new_users_last_month = db.query(User).filter(User.creationdate >= one_month_ago).count()

        # Calculate the percentage of new users in the last month
        stats["new_users_percentage_last_month"] = (new_users_last_month / stats["total_users"]) * 100 if stats["total_users"] > 0 else 0

        return stats
