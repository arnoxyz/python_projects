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

    while True:
        response = input("enter key [0,25] -> ").lower()
        if response.isdigit():
            config["key"] = int(response)
            break
        print("Wrong Input! Please enter a valid input => '0,1,2,...,25");

    response = input("enter text -> ")
    config["input_text"] = response
    return config


def main():
    config = {
            "encrypt" : True,
            "key" : 1,
            "input_text" : ""
    }

    config = user_input(config)
    print(config)

    copy_text_to_clipboard(config["input_text"])

main()
