from win32gui import GetWindowText,GetForegroundWindow
from time import sleep

def get_window_title() ->str :
    return GetWindowText(GetForegroundWindow()) # Get the title of the currently active window

def repeatedFunction(function,interval:int):
    '''
    It does not work with a thread automatically, so run it like this:
    import threading
    threading.Thread(target=repeatedFunction, args=(targetFunc, interval)).start()
    '''
    while True:
        sleep(interval)
        function()