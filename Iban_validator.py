
iban = input("Enter IBAN, please :")        # Input
iban = iban.replace('', '')                 # replace space
print("Replace-->", iban)

if not iban.isalnum():                              # Condition check
    print("You have enter invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short")
elif len(iban) > 31:
    print("IBAN entered is too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()       # convert to upper case
    print("___",iban)
    iban2 = ''
    for ch in iban:                             # loop
        if ch.isdigit():                        # check digit
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
            print("letter to number :",iban2)
    iban = int(iban2)
    print(iban)
    if iban % 97 == 1:
        print("IBAN is valid")
    else:
        print("IBAN is invalid")
