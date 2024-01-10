from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg = target_function(*args, **kwargs)
        return msg + " Please!!!"
    return wrapper


@beg
def say():
    msg = "Can you buy me Samosa"
    return msg


print(say())