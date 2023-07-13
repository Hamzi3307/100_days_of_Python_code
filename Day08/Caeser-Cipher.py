import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def cipher(code, jump, ncd_or_dcd):
    newtext = ''
    if ncd_or_dcd == 'D':
        jump *= -1
    for i in code:
        if i not in alphabet:
            newtext+=i
            continue
        index = alphabet.index(i)
        new_index = index + jump
        if new_index > 25:
            newtext += alphabet[new_index % 26]
        elif new_index >= 0 :
            newtext += alphabet[new_index]
        else:
            newtext += alphabet[new_index % 26]
    print(newtext)

while(True):
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").upper()
    if direction not in ['D','E']:
        print('Invalid Entry')
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(text, shift, direction)
