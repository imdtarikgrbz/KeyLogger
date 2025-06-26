import smtplib,ssl
import psw
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Email:
    def __init__(self) -> None:
        self.SMTP_SERVER= "smtp.gmail.com"  # Replace with your SMTP server
        self.SMTP_PORT = 587  # Use 465 for SSL or 587 for TLS
        self.USERNAME = psw.email  # Your email login
        self.PASSWORD = psw.psw  # Your email password
        
    def send_email(self,sender_email,receiver_email:str,subject:str,body:str,attachment=None) -> None:
        message = MIMEMultipart()
        message["From"] = psw.email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Attach email body
        message.attach(MIMEText(body, "plain"))
        
        # Attach file
        with open(attachment, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)  # Encode to base64
        part.add_header("Content-Disposition", f"attachment; filename={attachment}")  # Manually set file name
        message.attach(part)  # Attach the file to the email

        context = ssl.create_default_context()
        # Send email
        with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.USERNAME, self.PASSWORD)
            server.sendmail(sender_email, receiver_email, message.as_string())





if __name__ == "__main__":
    app = Email()
    app.send_email(receiver_email = psw.email,
                    sender_email= psw.email,
                    subject = "Email with Attachment",
                    body = "Hello, please find the attached file.",
                    attachment="./LOGS/logs.log")