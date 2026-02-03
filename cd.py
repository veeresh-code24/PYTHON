import sys

print("ARGV:", sys.argv)

if len(sys.argv) != 3:
    print("Usage: python3 cd.py <num1> <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Result:", num1 / num2)
