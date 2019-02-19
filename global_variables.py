x = 2

# First print
print(x)


def multiply_x_by_2():
    global x
    x = x * 2

    # third print
    print(x)


# second print
print(x)
multiply_x_by_2()


# DIVIDER #################################

def outer_function():
    y = 1

    def inner_function():
        nonlocal y
        y += 3
        print('inner_function:', y)

    inner_function()
    print('outer_function:', y)


outer_function()
