# Implementaion of CaesarCipher
text = input("Insert Text -> ")
shift = input("Shift Amount -> ")

def shift_text(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            current_position = ord(char) - base
            new_position = (current_position + shift) % 26
            result += chr(new_position + base)
        else:
            result += char
    return result

print("Input Text: " + text)
print("Output Text: " + shift_text(text, int(shift)))
