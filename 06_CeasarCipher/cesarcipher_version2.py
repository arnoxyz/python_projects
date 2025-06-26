# Other implemenation of CesarCipher
# added Feature: Copy result to the clipboard
try:
    import pyperclip
except ImportError:
    print("pyperclip not installed, so output will not be copied to clipboard...");

try:
    pyperclip.copy("Hello World!")
    print("Output copied to clipboard");
except:
    pass
