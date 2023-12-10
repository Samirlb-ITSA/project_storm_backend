from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from config.db_config import get_db_connection
from models.user_model import User
from models.job_offer_model import JobOffer
from models.applicant_model import Applicant
from models.company_model import Company
from models.role_model import Role
from datetime import datetime, timedelta

class StatisticsController:
    def __init__(self):
        self.db = None

    def get_db(self):
        self.db = get_db_connection()
        return self.db

    def close_db(self):
        if self.db is not None:
            self.db.close()

    def get_total_users(self):
        db = self.get_db()
        try:
            return db.query(User).count()
        finally:
            self.close_db()

    def get_active_job_offers(self):
        db = self.get_db()
        try:
            return db.query(JobOffer).filter(JobOffer.status == True).count()
        finally:
            self.close_db()

    def get_companies(self):
        db = self.get_db()
        try:
            return db.query(Company).limit(5).all()
        finally:
            self.close_db()

    def get_total_job_offers(self):
        db = self.get_db()
        try:
            return db.query(JobOffer).count()
        finally:
            self.close_db()

    def get_new_job_offers_last_month(self):
        db = self.get_db()
        try:
            one_month_ago = datetime.now() - timedelta(days=30)
            total_job_offers = db.query(JobOffer).count()
            new_job_offers = db.query(JobOffer).filter(JobOffer.status == True, JobOffer.creationdate >= one_month_ago).count()
            return (new_job_offers / total_job_offers) * 100 if total_job_offers else 0
        finally:
            self.close_db()

    def get_new_users_last_month(self):
        db = self.get_db()
        try:
            one_month_ago = datetime.now() - timedelta(days=30)
            total_users = db.query(User).count()
            new_users = db.query(User).filter(User.creationdate >= one_month_ago).count()
            return (new_users / total_users) * 100 if total_users else 0
        finally:
            self.close_db()

    def get_users_applied_to_jobs_count(self):
        db = self.get_db()
        try:
            return db.query(User).join(Applicant, User.userid == Applicant.userid).distinct().count()
        finally:
            self.close_db()

    def get_total_companies(self):
        db = self.get_db()
        try:
            return db.query(Company).count()
        finally:
            self.close_db()

    def get_job_offers_by_year(self):
        db = self.get_db()
        try:
            current_year = datetime.now().year
            last_year = current_year - 1
            job_offers_current_year = [0]*12
            job_offers_last_year = [0]*12
            job_offers = db.query(JobOffer).all()
            for job_offer in job_offers:
                if job_offer.creationdate.year == current_year:
                    job_offers_current_year[job_offer.creationdate.month - 1] += 1
                elif job_offer.creationdate.year == last_year:
                    job_offers_last_year[job_offer.creationdate.month - 1] += 1
            return job_offers_current_year, job_offers_last_year
        finally:
            self.close_db()

    def get_users_by_roles(self):
        db = self.get_db()
        try:
            roles = db.query(Role).all()
            users_by_roles = {}
            for role in roles:
                users_by_roles[role.name] = db.query(User).join(User.roles).filter(Role.name == role.name).count()
            return users_by_roles
        finally:
            self.close_db()

    def get_roles_count(self):
        db = self.get_db()
        try:
            roles = db.query(Role).all()
            roles_count = {}
            for role in roles:
                role_users_count = db.query(User).join(User.roles).filter(Role.roleid == role.roleid).count()
                roles_count[role.name] = role_users_count
            return roles_count
        finally:
            self.close_db()

    def get_user_statistics(self):
        stats = {
            "total_users": self.get_total_users(),
            "new_users_last_month": self.get_new_users_last_month(),
            "users_applied_to_jobs_count": self.get_users_applied_to_jobs_count(),
            "users_by_roles": self.get_users_by_roles(),
            "roles_count": self.get_roles_count()
        }
        return stats

    def get_job_statistics(self):
        job_offers_current_year, job_offers_last_year = self.get_job_offers_by_year()
        stats = {
            "active_job_offers": self.get_active_job_offers(),
            "total_job_offers": self.get_total_job_offers(),
            "new_job_offers_last_month": self.get_new_job_offers_last_month(),
            "total_companies": self.get_total_companies(),
            "job_offers_current_year": job_offers_current_year,
            "job_offers_last_year": job_offers_last_year
        }
        return stats

    def get_company_statistics(self):
        stats = {
            "companies": self.get_companies(),
        }
        return stats