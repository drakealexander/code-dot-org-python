"""Stage 7: Puzzle 7 of 11

Here's the code for drawing the square from last puzzle. Can you repeat
it to draw 10 adjacent squares like a ladder? Hint: you only need 2
more lines of code.

"""

import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('s1level41')

# TODO draw 10 adjacent squares like a ladder in 8 lines of code or less
artist.color = 'random'
for count in range(4):
    artist.move_forward(20)
    artist.turn_right(90)

artist.check()
