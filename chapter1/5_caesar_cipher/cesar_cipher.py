# Implementaion of CaesarCipher
text = input("Insert Text -> ")
shift_amount = input("Shift Amount -> ")
which_way = input("E = Encrypt (default) or D = Decrypt text? -> ")

while not shift_amount.isdigit():
    print("Error please insert a valid integer [0,25]")
    shift = input("Shift Amount -> ")

def shift(text, shift_amount, which_way):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            current_position = ord(char) - base
            if (which_way == "D"):
                #decrypting, <- shift
                new_position = (current_position - shift_amount) % 26
            else:
                #encrypting, shift ->
                new_position = (current_position + shift_amount) % 26
            result += chr(new_position + base)
        else:
            result += char
    return result

print("Input Text:  " + text)
print("Output Text: " + shift(text, int(shift_amount), which_way))
