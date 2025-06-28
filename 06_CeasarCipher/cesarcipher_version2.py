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
def user_input(config):
    while True:
        response = input("(e)ncrypt or (d)ecrypt? -> ").lower()
        if response.startswith('e'):
            #set config -> 'e'
            config["encrypt"] = True
            break
        elif response.startswith('d'):
            #set config -> 'd' decrypt
            config["encrypt"] = False
            break
        print("Wrong Input! Please enter a valid input => 'e' or 'd'");
    # TODO: User Input: Key (shift number) number % 26
    # TODO: User Input: Text (the text that should get en-/decrypted
    return config


def main():
    config = {
            "encrypt" : True
    }

    config = user_input(config)
    print(config)

    # TODO: Text processing and saving/outputing result
    copy_text_to_clipboard(text)

main()
