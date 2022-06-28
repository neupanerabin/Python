line = input("Enter a line of numbers: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        substr = float(substr)
        total += substr
    print("The total is :", total)
except:
    print(substr ," is not a number")
