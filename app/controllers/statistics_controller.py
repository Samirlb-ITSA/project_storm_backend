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
            "active_job_offers_per_user": 0,
            "new_job_offers_percentage_last_month": 0,
            "total_users": 0,
            "new_users_percentage_last_month": 0,
            "users_applied_to_jobs_count": 0,
        }

        # Count the number of active job offers
        active_job_offers_count = db.query(JobOffer).filter(JobOffer.status == 1).count()
        stats["active_job_offers_per_user"] = active_job_offers_count

        # Count the total number of job offers
        stats["total_job_offers"] = db.query(JobOffer).count()

        # Count the total number of users
        stats["total_users"] = db.query(User).count()

        # Count the total number of job offers created in the last month
        one_month_ago = datetime.now() - timedelta(days=30)
        new_job_offers_last_month = db.query(JobOffer).filter(JobOffer.status == 1, JobOffer.creationdate >= one_month_ago).count()

        # Calculate the percentage of new job offers in the last month
        stats["new_job_offers_percentage_last_month"] = round((new_job_offers_last_month / stats["total_job_offers"]) * 100) if stats["total_job_offers"] > 0 else 0

        # Count the total number of users registered in the last month
        new_users_last_month = db.query(User).filter(User.creationdate >= one_month_ago).count()

        # Calculate the percentage of new users in the last month
        stats["new_users_percentage_last_month"] = round((new_users_last_month / stats["total_users"]) * 100) if stats["total_users"] > 0 else 0

        # Count users who have applied to job offers
        users_applied_to_jobs_count = db.query(User).join(Applicant, User.userid == Applicant.userid).distinct().count()
        stats["users_applied_to_jobs_count"] = users_applied_to_jobs_count

        return stats
