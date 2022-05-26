def prime(fn):
    """
    Decorator for FSM class methods.
    """
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper
    