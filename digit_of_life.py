date = int(input("Enter date of birth in YYMMDD: "))
splite = [int(x) for x in str(date)]
sum = 0
#print(splite)
for i in splite:
    sum =sum+ i
#print(sum)

no = [int(x) for x in str(sum)]
add = 0
for j in no:
    add = add + j
print(add)


