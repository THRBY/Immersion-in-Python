import sys

digit_string = sys.argv[1]

sum_d = 0
for i in digit_string:
	i = int(i)
	sum_d += i

print(sum_d)
