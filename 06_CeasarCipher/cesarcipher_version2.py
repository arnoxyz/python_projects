# Other implemenation of CesarCipher
# added Feature: Copy result to the clipboard
try:
    import pyperclip
except ImportError:
    print("pyperclip not installed, so output will not be copied to clipboard...")

def copy_text_to_clipboard(text):
    try:
        pyperclip.copy("Hello World!")
        print("Output copied to clipboard")
    except:
        pass

text = "User Text!"
# User Input: Encrypt/Decrypt
# User Input: Key (shift number) number % 26
# User Input: Text (the text that should get en-/decrypted
# Text processing and saving/outputing result

copy_text_to_clipboard(text)
