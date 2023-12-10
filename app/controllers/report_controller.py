from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

class ReportController:
    def __init__(self):
        template_path =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources'))
        self.env = Environment(loader=FileSystemLoader(template_path))
        self.template = self.env.get_template("report_template.html")

    def generate_report(self, user_stats, job_stats, company_stats):
        # Render the statistics into the HTML template
        html_content = self.template.render(user_stats=user_stats, job_stats=job_stats, company_stats=company_stats)

        # Create a new PDF document and add the HTML content
        with open("report.pdf", "w+b") as result_file:
            pisa_status = pisa.CreatePDF(html_content, dest=result_file)

        return "report.pdf" if not pisa_status.err else "Error generating PDF"