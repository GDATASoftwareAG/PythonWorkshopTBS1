class SimpleObjectForDemoPurpose:
    number = 2


def main():
    number = 2

    # Simple If-Statement
    if number == 2:
        print('Number = 2.')

    # If-Statement with else-if and else
    if number < 2:
        print('Number < 2.')
    elif number > 2:
        print('Number > 2.')
    else:
        print('Number = 2.')

    # If-Statement with boolean
    boolean = True
    boolean2 = False
    if boolean:
        print('Boolean is True.')
    else:
        print('Boolean is False.')

    # If-Statement with boolean combination using keywords 'not', 'and' and 'or'
    if boolean and boolean2:
        print('Both booleans are True.')
    elif boolean and not boolean2:
        print('Only the first boolean is True.')
    elif not boolean and boolean2:
        print('Only the second boolean is True.')
    else:
        print('Both booleans are False.')

    if boolean or boolean2:
        print('One of the booleans is True.')

    # If-Statements to check if the second statement will be executed to evaluate the condition
    print('Start evaluation. True or False.')
    if function_to_show_print_with_returned_boolean(True) or function_to_show_print_with_returned_boolean(False):
        pass
    print('Finished evaluation')

    print('Start evaluation. False or True.')
    if function_to_show_print_with_returned_boolean(False) or function_to_show_print_with_returned_boolean(True):
        pass
    print('Finished evaluation')

    print('Start evaluation. False or False.')
    if function_to_show_print_with_returned_boolean(False) or function_to_show_print_with_returned_boolean(False):
        pass
    print('Finished evaluation')

    # Same with 'and'
    print('Start evaluation. True and False.')
    if function_to_show_print_with_returned_boolean(True) and function_to_show_print_with_returned_boolean(False):
        pass
    print('Finished evaluation')

    print('Start evaluation. False and True.')
    if function_to_show_print_with_returned_boolean(False) and function_to_show_print_with_returned_boolean(True):
        pass
    print('Finished evaluation')

    print('Start evaluation. False and False.')
    if function_to_show_print_with_returned_boolean(False) and function_to_show_print_with_returned_boolean(False):
        pass
    print('Finished evaluation')

    # Compare strings
    string = 'hello'
    if string == 'hello':
        print('Greetings.')

    if string != 'world':
        print('No world found.')

    # Conditionals on objects
    simple_object = SimpleObjectForDemoPurpose()
    simple_object2 = SimpleObjectForDemoPurpose()
    if simple_object:
        print('This is the same statement as "if simple_object != None:"')

    if simple_object == simple_object:
        print('Should be the same')

    if simple_object != simple_object2:
        print('Not the same object even when values in object are the same')

    if simple_object.number == simple_object2.number:
        print('Values from objects are the same')


def function_to_show_print_with_returned_boolean(boolean: bool) -> bool:
    print('Execution of function_to_show_print_with_returned_boolean(boolean).')
    return boolean


if __name__ == '__main__':
    main()
