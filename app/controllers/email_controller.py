# controllers/email_controller.py

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from jinja2 import Environment, FileSystemLoader

async def send_email(to_email: str, subject: str, password: str):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "ubarranquillaegresados@gmail.com"
    smtp_password = "mjleulsxjcpymssl"
    from_email = "ubarranquillaegresados@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Bienvenido usuario Unibarranquilla"

  # Load Jinja2 template
    file_loader = FileSystemLoader('Resources')
    env = Environment(loader=file_loader)
    template = env.get_template('body.html')

   # Render the template with data
    body = template.render(email=to_email, password=password)       

    # Attach the body of the email
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": f"Error sending email: {e}"}
