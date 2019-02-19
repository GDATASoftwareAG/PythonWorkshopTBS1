def a_function():
    print("I will be printed every time somebody calls a_function, wether it's my main or somebody else.")
    return 1


def unit_test():
    print("I will only be called when my python module is being executed directly.")
    print("This is a very basic unit test.")
    assert a_function() == 1, "Something impossible happened"
    print("Unit test passed.")


if __name__ == "__main__":
    unit_test()
