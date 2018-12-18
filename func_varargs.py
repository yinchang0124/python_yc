def total(a=5, *numbers, **phonebook):
    print("a=", a)

    for single_item in numbers:
        print("single_item", single_item)

    for first, second in phonebook.items():
        print(first, second)


print(total(10, 1, 2, 3, 4, jack=1243, helen=2322, tom=2343))