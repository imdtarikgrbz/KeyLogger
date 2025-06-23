from win32gui import GetWindowText,GetForegroundWindow 

def get_window_title() ->str :
    return GetWindowText(GetForegroundWindow()) # Get the title of the currently active window
    
