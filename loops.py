def main():
    # Normal for-i loop
    for i in range(5):
        print('Value of i is', i)

    # Looping through an array
    array = ['hello', 'my', 'name', 'is', 'John']
    for word in array:
        print('\t', word)

    # looping through a list
    a_list = list()
    a_list.append('Peter')
    a_list.append('Maria')
    a_list.append('John')
    for name in a_list:
        print('Hello', name)

    # simple while loop
    number = 0
    while number < 10:
        print('Number value', number)
        number += 1

    # unpack nested data
    nested_data_array = [
        ('colors', ['red', 'blue', 'orange', 'yellow']),
        ('animals', ['cow', 'tiger', 'fish', 'dog'])
    ]
    for (identifier, values) in nested_data_array:
        for value in values:
            print(identifier, ':', value)

    # unpack dictionary
    dictionary = {
        'username': 'admin',
        'password': '1234',
        'url': 'localhost:8080'
    }
    for key in dictionary.keys():
        print(key, ':', dictionary.get(key))

    for value in dictionary.values():
        print(value)

    for key, value in dictionary.items():
        print(key, ':', value)

    for entry in dictionary:
        print(entry, ':', dictionary[entry])


    # inline loops e.g. for filters
    numbers = [1, 2, 3, 4]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(even_numbers)
    odd_numbers = [x for x in numbers if x % 2 != 0]
    print(odd_numbers)

    # nested inline loops
    letters = ['a', 'b', 'c']
    letters_combined = [n * letter for n in numbers for letter in letters]
    print(letters_combined)


if __name__ == '__main__':
    main()
