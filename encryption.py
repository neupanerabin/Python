text = input("Enter your message :")
cipher = ' '
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord("A")
    cipher += chr(code)
print(cipher)

text = input("Enter cipher text :")
text = ' '
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)

