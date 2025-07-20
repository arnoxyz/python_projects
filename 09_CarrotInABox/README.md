# Carrot-in-a-Box - Game
This is my implementation so I use to draw an apple instead of a carrot because I like apples more.
## How it works
There are two players and everyone gets a box. In one of the boxes there is a price. The goal is to get the price. Player1 is allowed to look inside both boxes and see where the price is hiding. Meanwhile Player2 is not allowed to take a look, so the eyes are closed. Then the second player can decide to switch boxes or not. So the
secod player has to look at the first player and see if the player is bluffing or not. After that the players can look in their boxes and see who won.
## Example:
### Intro
```
python3 appleinabox.py
Welcome to Apple in a Box!
-PLAYER 1-  -PLAYER 2-
+--------+  +--------+
|        |  |        |
|  BOX1  |  |  BOX2  |
|        |  |        |
+--------+  +--------+

Player 2 please close your eyes... (Press Enter to Continue)
```
### Player1 turn
```
-PLAYER 1-  -PLAYER 2-

               (---)
|        |  |        |
|  BOX1  |  |  BOX2  |
|        |  |        |
+--------+  +--------+

Player 1 at the moment you got the box with no apple
Player 1 if you are done ... (Press Enter to Continue)
```
### Player2 turn
```

-PLAYER 1-  -PLAYER 2-
+--------+  +--------+
|        |  |        |
|  BOX1  |  |  BOX2  |
|        |  |        |
+--------+  +--------+

Player 2 can decide now to switch the boxes or not -> Switch Boxes? (y/n): y

```
### Final
```
-PLAYER 2-  -PLAYER 1-

  (---)
|        |  |        |
|  BOX1  |  |  BOX2  |
|        |  |        |
+--------+  +--------+

Player 1 Won
```
