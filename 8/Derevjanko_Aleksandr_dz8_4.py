def val_checker(func):
    def callback(number):
        if number < 0:
            raise ValueError(f'wrong val {number}')
        else:
            return func(number)
    return callback


@val_checker
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
