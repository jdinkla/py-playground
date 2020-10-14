def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def double(func):
    def wrapper():
        original_result = func()
        modified_result = "".join([f"{x}{x}" for x in original_result])
        return modified_result
    return wrapper


@uppercase
@double
def greet():
    return 'Hello!'


print(greet())
