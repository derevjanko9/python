def type_logger(func):
    def wrapper_type_logger(x):
        result = type(x)
        return f'{func(x)}: {result}'
    return wrapper_type_logger


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
