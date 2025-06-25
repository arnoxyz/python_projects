# Ceasar Cipher
Way to easy encrypt messages by shifting the alphabet by a specific number. Now the encrypted output can be transmitted. To decrypt the output, the receiver needs the specfic number, then just shifts back the alphabet and can read the message.

## Decrypting by Shifting the alphabet
This shifting can be now any number of the alphabet. Until
the number is as big as the alphabet length. This starts it over like
an modulo operation. So all possible shifted alphabets are limited by the
number of letters in it:
- A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Has 26 letters so there are possible 26 different shifts. So ShiftNumber mod 26
- A -> A (shift by 0 or 26 or 42 or 64 ...)
- A -> B (shift by 1, or 27, ...)
- A -> C (shift by 2, or 28, ...)
- A -> D (shift by 3, ...)
- A -> E (shift by 4, ...)
- ...
- A -> Z (shift by 25, ...)
- A -> A (shift by 26, or 0)
### Example:
A shift by 1 means: So if you input ABC the output will be: BCD
- (A -> B, B -> C, C -> D, ... ,  Z -> A)


## Implementation using ord(), char()
ord() = converts char to ASCII code,       example: ord("D") -> 68
char() = converts ASCII code back to char, example: char(68) -> "D"

### Normalize to make it easy to shift:
ord('A') = 65, becomes 0, 'B' then 1
To get this behavior just subract the base value. Then the shifting of that relative position.
```
current_position = ord(char) - base
new_position = (current_position + shift) % 26
```
At the end to convert back to character you need to add the base back to the current
value.
```
result += chr(new_position + base)
```
## Example
### Encrypt Message
```
Insert Text -> Arno
Shift Amount -> 3
E = Encrypt (default) or D = Decrypt text? -> E
Input Text:  Arno
Output Text: Duqr
```
### Decrypt Message
```
Insert Text -> Duqr
Shift Amount -> 3
E = Encrypt (default) or D = Decrypt text? -> D
Input Text:  Duqr
Output Text: Arno
```
