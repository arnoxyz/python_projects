[Back](../../)
# Bitmap Message
A bitmap is a way to represent a picture. The "map" is a big 2D Array where each element
has a value. To make it easy this element has only two values (a bit). With this it is eays to save a black and white picture as just an 2D Array with values like [0,1,1,1,0,0,0...] and so on.

This implementation uses a string to save and represent text. As 0 value so the white dot here the character ' ' so just an empty space is used. All other values so the 1 value is represented as a character. Example 'A'

It is also possible to implement it with more characters, the characters would then just repeat itself. Example "Test" saved then in the string array for every 'A' or better every non ' '.

Example: [0,1,1,1,0,0,0,1,1,0,1] would be
         [' ','T','e','s',' ',' ',' ', 't', 'T', 'e',' ','s']
