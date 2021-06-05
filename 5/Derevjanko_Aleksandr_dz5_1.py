def nums_generator(n):
    for num in range(1, n + 1, 2):
        yield num


print(list(nums_generator(15)))
