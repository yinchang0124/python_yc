import sys

print("The command line arguments are:")

for i in sys.argv:
    print(i)


print("\n\n python is", sys.path, "\n")

from math import sqrt
print("Square root of 16 is", sqrt(16))
