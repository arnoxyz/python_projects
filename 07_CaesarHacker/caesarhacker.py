# Implementaion of

def decrypt_text(key, input_text):
    Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output_text = "";

    for char in input_text:
        if char == " ":
            output_text = output_text + " "
            continue
        num = Characters.find(char)
        num = (num - key) % 26
        output_text = output_text + Characters[num]
    return output_text;

def output_to_user(config):
    print("Output_Text: -> " + config["output_text"] + " (KEY= " + str(config["key"]) + ")")

def main():
    config = {
            "encrypt" : True,
            "key" : 1,
            "input_text" : "",
            "output_text" : ""
    }

    config["input_text"] = input("Input cesar encrypted text -> ")
    config["output_text"] = decrypt_text(config["key"], config["input_text"])
    output_to_user(config)

main()
