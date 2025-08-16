# Caesar Hacker
Way to brute force decrypt a messages that is encrypted with caesar cipher.
So cracking the code withouth knowing the key, that the message was encrypted with.

## Brute Force Method
Print out all 26 ways to decrypt the message.


## Example
### Encrypt
Encrypt a message using caesarcipher program from previous project.
```
Output_Text: -> JXYI YI Q IYCFBU JUIJ
```
### Decrypt
What is the message? Decrypting using caesar hacker program:

```
~/Projects/07_CaesarHacker$ python3 caesarhacker.py
Input cesar encrypted text -> JXYI YI Q IYCFBU JUIJ
Output_Text: -> JXYI YI Q IYCFBU JUIJ (KEY= 0)
Output_Text: -> IWXH XH P HXBEAT ITHI (KEY= 1)
Output_Text: -> HVWG WG O GWADZS HSGH (KEY= 2)
Output_Text: -> GUVF VF N FVZCYR GRFG (KEY= 3)
Output_Text: -> FTUE UE M EUYBXQ FQEF (KEY= 4)
Output_Text: -> ESTD TD L DTXAWP EPDE (KEY= 5)
Output_Text: -> DRSC SC K CSWZVO DOCD (KEY= 6)
Output_Text: -> CQRB RB J BRVYUN CNBC (KEY= 7)
Output_Text: -> BPQA QA I AQUXTM BMAB (KEY= 8)
Output_Text: -> AOPZ PZ H ZPTWSL ALZA (KEY= 9)
Output_Text: -> ZNOY OY G YOSVRK ZKYZ (KEY= 10)
Output_Text: -> YMNX NX F XNRUQJ YJXY (KEY= 11)
Output_Text: -> XLMW MW E WMQTPI XIWX (KEY= 12)
Output_Text: -> WKLV LV D VLPSOH WHVW (KEY= 13)
Output_Text: -> VJKU KU C UKORNG VGUV (KEY= 14)
Output_Text: -> UIJT JT B TJNQMF UFTU (KEY= 15)
Output_Text: -> THIS IS A SIMPLE TEST (KEY= 16)
Output_Text: -> SGHR HR Z RHLOKD SDRS (KEY= 17)
Output_Text: -> RFGQ GQ Y QGKNJC RCQR (KEY= 18)
Output_Text: -> QEFP FP X PFJMIB QBPQ (KEY= 19)
Output_Text: -> PDEO EO W OEILHA PAOP (KEY= 20)
Output_Text: -> OCDN DN V NDHKGZ OZNO (KEY= 21)
Output_Text: -> NBCM CM U MCGJFY NYMN (KEY= 22)
Output_Text: -> MABL BL T LBFIEX MXLM (KEY= 23)
Output_Text: -> LZAK AK S KAEHDW LWKL (KEY= 24)
Output_Text: -> KYZJ ZJ R JZDGCV KVJK (KEY= 25)
```
#### Solution:
The key is 16 and the message is:
```
Output_Text: -> THIS IS A SIMPLE TEST (KEY= 16)
```
