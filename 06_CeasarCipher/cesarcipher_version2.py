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
        response = input("enter key [0,25] -> ")
        if response.isdigit():
            config["key"] = int(response)
            break
        print("Wrong Input! Please enter a valid input => '0,1,2,...,25");

    response = input("enter text -> ")
    config["input_text"] = response.upper()
    return config

def encrypt_text(key, input_text):
    Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output_text = "";

    for char in input_text:
        num = Characters.find(char)
        num = (num + key) % 26
        output_text = output_text + Characters[num]
    return output_text;

def output_to_user(config):
    print("... ------Done------ ...")
    print("Input_Text:  -> " + config["input_text"])
    print("Output_Text: -> " + config["output_text"])
    copy_text_to_clipboard(config["output_text"])

def main():
    # fixed input values (for debugging now)
    config = {
            "encrypt" : True,
            "key" : 1,
            "input_text" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "output_text" : ""
    }
    #config = user_input(config)
    print(config)

    if config["encrypt"]:
        print("... encrypting input now ...")
        config["output_text"] = encrypt_text(config["key"], config["input_text"])
    else:
        print("... decrypting input now ...")
        #TODO:
        #config["output_text"] = dencrypt_text(config["key"], config["input_text"])

    output_to_user(config)

main()
