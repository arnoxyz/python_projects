# Implementation of Bitmap Message
# Displays a user input text in a given bitmap by replacing symbols in the bitmap with the given input symbols.

# Example the Austria Flag
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


#replace_with = "Austria"
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
    
