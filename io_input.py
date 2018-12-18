def reverse(text):
    return text[::-1]

def is_plaindrom(text):
    return text == reverse(text)


something = input("enter text:")
if is_plaindrom(something):
    print("yes")
else:
    print("no")