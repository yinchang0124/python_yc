x = 66


def func():
    global x

    print("x is", x)
    x = 3
    print("change global x to", x)


func()
print("x still is", x)