# Implementaion of CaesarCipher

text = "Hello World!"
print("Input Test: " + text)


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
            #need to add back the base to get the right ascii number
            result += chr(new_position + base) 
        else:
            result += char
    return result


print("Output Text: " + shift_text(text, 16))
