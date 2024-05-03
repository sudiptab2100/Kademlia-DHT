import threading


def setInterval(sec, func, *args):
    """
    Calls the given function repeatedly with a fixed time interval.
    
    Args:
        sec (float): The time interval in seconds between each function call.
        func (function): The function to be called repeatedly.
        *args: Variable length argument list to be passed to the function.
    
    Returns:
        threading.Timer: The timer object that can be used to cancel the interval.
    
    """
    def func_wrapper():
        setInterval(sec, func, *args)
        func(*args)
    
    t = threading.Timer(sec, func_wrapper)
    t.start()
    
    return t
