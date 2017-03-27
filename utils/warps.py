from functools import wraps


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if current_user() is None:
            return redirect(url_for('user.index'))
        return f(*args, **kwargs)
    return function
