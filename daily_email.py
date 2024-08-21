import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

def send_daily_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Daily Report"

    body = """
    <html>
      <body>
        <h1>Daily Report</h1>
        <p>Hey, this is Akshat from Hack Club. Have fun coding!</p>
      </body>
    </html>
    """
    message.attach(MIMEText(body, 'html'))

    filename = "report.pdf"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        message.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

schedule.every().day.at("08:00").do(send_daily_email)

while True:
    schedule.run_pending()
    time.sleep(60)