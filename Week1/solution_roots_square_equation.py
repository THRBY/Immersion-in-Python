import sys
import math

digit_string = int(sys.argv[1])

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c

if __name__ == "__main__":
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(int(x1))
        print(int(x2))
    elif d == 0:
        x1 = x2 = -b/(2*a)
        print(int(x1))
        print(int(x2))
    else:
        print("Error")
