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
            config["encrypt"] = True
            break
        elif response.startswith('d'):
            config["encrypt"] = False
            break
        print("Wrong Input! Please enter a valid input => 'e' or 'd'");

    # User Input: Key (shift number) number % 26
    while True:
        response = input("enter key [0,25] -> ").lower()
        if response.isdigit():
            config["key"] = int(response)
            break
        print("Wrong Input! Please enter a valid input => '0,1,2,...,25");
    # TODO: User Input: Text (the text that should get en-/decrypted
    return config


def main():
    config = {
            "encrypt" : True,
            "key" : 1
    }

    config = user_input(config)
    print(config)

    # TODO: Text processing and saving/outputing result
    copy_text_to_clipboard(text)

main()
