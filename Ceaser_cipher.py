checkText = False
while checkText != True:
    text = input("Enter your message :")
    if text != '':
        checkText = True

checkShift = False
shiftNumber = list(range(1,26))
while checkShift != True:
    try:
        shift = int(input("Enter your shift number(1~25: "))
        if shift in shiftNumber:
            checkShift = True

    except:
        print("Please Enter number between 1 and 25 !!")
        continue

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    if char.islower():
        code = ord(char) + shift
        if code > ord('z'):
            code = ord('a') + (code - ord('z') - 1)
        cipher += chr(code)

    if char.isupper():
        code = ord(char) + shift
        if code > ord('Z'):
            code = ord('A') + (code- ord('Z') - 1)
        cipher += chr(code)

print(cipher)

# link for more details https://itcosmos.co/improving-the-caesar-cipher-with-python/