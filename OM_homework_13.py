'''
1.Write a decorator that ensures a function is only called by users with a specific role.
Each function should have a user_type with a string type in kwargs
'''
def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper
'''
2. Write a decorator that wraps a function in a try-except block and print an error if error has happened
'''
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error_type:
            print(f'Error happened: {error_type}')
    return wrapper

'''
4. Create a function that caches the result of a function, so that if it is called with same same argument \
multiple times, it returns the cached result first instead of re-executing the function. 
'''
def cache_result(func):
    cache = dict()
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper
