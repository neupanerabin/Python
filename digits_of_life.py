date = input("Enter  your birthday : ")

if len(date) != 8 or not date.isdigit():
    print("Invalid date format")

else:
    while len(date) > 1:
        sum = 0
        for dig in date:
            sum += int(dig)
            print(sum)
        date = str(sum)
    print("Your Digit of Life is :" + date)