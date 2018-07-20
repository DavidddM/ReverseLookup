def no_data_decorator(func):
    def wrapper(data):
        if data is None:
            return None
        return func(data)
    return wrapper
