# “ab”是地址（Address）簿（Book）的缩写
ab = {
    "1": "hhhh",
    "2": "xixixiix",
    "3": "lalala"
}

print("1:", ab["1"])

del ab["2"]

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for num, add in ab.items():
    print("{} is {}".format(num, add))


ab["4"] = "kkkkk"

if "4" in ab:
    print("\n4 is", ab["4"])