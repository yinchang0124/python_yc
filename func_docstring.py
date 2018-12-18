def print_max(x, y):
    '''打印两个数值中的最大数。


这两个数都应该是整数'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is bigger")
    else:
        print(y, "is bigger")


print_max(4, 5)
print(print_max.__doc__)