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


@is_admin
def show_customer_receipt(user_type: str):
    if user_type == 'admin':
        print(f'Admin user is authorized to view receipt for customer')
    else:
        print(f'User is not authorized')


'''
2. Write a decorator that wraps a function in a try-except block and print an error if error has happened
'''


def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error_type:
            print(f"An error occurred during execution: {type(error_type).__name__}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})

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


@cache_result
def add(a: int, b: int) -> int:
    return a + b


print(add(2, 5))  # Output: 7 (calculated)
print(add(2, 5))  # Output: 7 (cached)
