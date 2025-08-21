[Back](../../)
# Cho-Han - Game
Even or odd dice game.
## How it works
Japanese gambling game: Two dice are thrown under a cup. Then the players can bet if the sum (cho) is even or odd (han). The house will also subtract a betting fee of 5 for every game.
### Example
```
python3 chohan.py
play another round of cho/han? (y)es/(n)o > yes
+-------+   +-------+
|       |   |       |
|       |   |       |
|       |   |       |
+-------+   +-------+
Your credit is 100
How much do you want to bet? > 50
Is the sum of the dice (E)ven or (O)dd? > e
+-------+   +-------+
| o   o |   | o   o |
|   o   |   | o   o |
| o   o |   | o   o |
+-------+   +-------+
sum is odd
play another round of cho/han? (y)es/(n)o > yes
+-------+   +-------+
|       |   |       |
|       |   |       |
|       |   |       |
+-------+   +-------+
Your credit is 45
How much do you want to bet? > 40
Is the sum of the dice (E)ven or (O)dd? > e
+-------+   +-------+
| o   o |   | o   o |
|   o   |   |   o   |
| o   o |   | o   o |
+-------+   +-------+
sum is even
You won! Your credit is now: 80
play another round of cho/han? (y)es/(n)o > no
Thanks for playing your final score is: 80
```


