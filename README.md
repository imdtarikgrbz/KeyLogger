# Keylogger Project

## Overview

This project is a modular keylogger written in Python. It captures keystrokes, logs them to files, and periodically sends the logs via email. The project is structured for educational and testing purposes.

---

## Features

- **Keystroke Logging:** Captures all keyboard input and logs it to a file.
- **Window Tracking:** Logs the active window title for context.
- **Periodic Emailing:** Sends log files as email attachments at configurable intervals.
- **Threaded Background Tasks:** Uses threads to run background tasks without blocking the main logger.
- **Configurable:** All settings (email, logging, intervals) are managed via `config.py`.

---

## Setup

1. **Install Requirements:**
   - Python 3.10+ recommended
   - Install dependencies:
     ```sh
        pip install pynput pywin32
     ```

2. **Configure Email:**
   - Edit `keylogger/config.py` with your email credentials.
   - For Gmail, you may need to create an [App Password](https://myaccount.google.com/apppasswords).An app password is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. App passwords can only be used with accounts that have 2-Step Verification turned on.

3. **(Optional) Change Logging Interval:**
   - Adjust `LOG_INTERVAL` in `config.py` (default: 5 * 60 seconds).

---

## Usage

### Run the Keylogger:
 ```sh
    pip install pynput pywin32
 ```
- This will start the background email task and the keylogger.
- Logs are saved in the `LOGS/` directory.

---

## Security Warning

> **Do NOT use this software for malicious purposes.**
>
> Only run this code on machines you own or have explicit permission to monitor.

---

## License

This project is for educational purposes only.

---

## Credits

- Keyboard capture: [pynput](https://pynput.readthedocs.io/)
- Window title: [pywin32](https://github.com/mhammond/pywin32)