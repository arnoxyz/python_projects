# Other implemenation of CesarCipher
# Uses different SYMOBLS so now also numbers and lowercase chars can be en/decrypted
SYMBOLS_ON_THE_WHEEL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789%€!?&%$§*+#"

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
        response = input("enter key -> ")
        if response.isdigit():
            config["key"] = int(response)
            break
        print("Wrong Input! Please enter a valid input => '0,1,2,....");

    response = input("enter text -> ")
    config["input_text"] = response
    return config

def process_text(key, input_text, encrypt):
    if encrypt == True:
        print("ecrypting input now ...")
    else:
        print("decrypting input now ...")

    output_text = "";

    for char in input_text:
        if char == " ":
            output_text = output_text + " "
            continue

        num = SYMBOLS_ON_THE_WHEEL.find(char)
        if encrypt == True:
            num = (num + key) % len(SYMBOLS_ON_THE_WHEEL)
        else:
            num = (num - key) % len(SYMBOLS_ON_THE_WHEEL)
        output_text = output_text + SYMBOLS_ON_THE_WHEEL[num]
    return output_text;

def output_to_user(config):
    print("Done")
    print("Input_Text:  -> " + config["input_text"])
    print("Output_Text: -> " + config["output_text"])
    copy_text_to_clipboard(config["output_text"])

def main():
    config = {
            "encrypt" : True,
            "key" : 3,
            "input_text" : "",
            "output_text" : ""
    }

    config = user_input(config)
    config["output_text"] = process_text(config["key"], config["input_text"], config["encrypt"])
    output_to_user(config)

main()
