str1 = input("Enter first stringsL :")
str2 = input("Enter second strings: ")

strx1 = ''.join(sorted(list(str1.upper().replace(' ', ' '))))
strx2 = ''.join(sorted(list(str2.upper().replace(' ', ' '))))

if(strx1 == strx2):
    print("Anagram")
else:
    print("Not an anagram")
