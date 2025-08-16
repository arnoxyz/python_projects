# Implementation of Bitmap Message
# Displays a user input text in a given bitmap by replacing symbols in the bitmap with the given input symbols.

# Example: the Austria Flag
bitmap = """


 ***********************************************************
 ***********************************************************
 ***********************************************************
 ***********************************************************
                                                            
                                                            
                                                            
                                                           
 ***********************************************************
 ***********************************************************
 ***********************************************************
 ***********************************************************


"""


def draw_bitmap(bitmap):
    replace_with = input("insert a word: ")
    j = 0;
    for i in bitmap:
        if i=='*':
            print(replace_with[j], end="")
            j=j+1
            if j == len(replace_with):
                j=0
        else:
            print(i, end="")

# Other version using modulo operator
def draw_bitmap2(bitmap):
    replace_with = input("insert a word: ")
    j = 0;
    for i in bitmap:
        if i=='*':
            print(replace_with[j % len(replace_with)], end="")
            j=j+1
        else:
            print(i, end="")


draw_bitmap(bitmap)
draw_bitmap2(bitmap)
