from functools import wraps


def user_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        print('=> user_required Middleware touch')
        return f(*args, **kwargs)

    return wrap
