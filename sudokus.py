def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

rows = []
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row : " + str(r + 1) + " :")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data -9 digits required")
        rows.append(row)
ok = True

#check if all rows are good
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

#check if all columns are good
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break
#check if all sub-squares (3 * 3)are good
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ' '
            #Make  a string containing all digits from a sub-square
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break
#Print the final verdict
if ok:
    print("Yes")
else:
    print("No")
#
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672