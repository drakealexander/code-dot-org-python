"""Stage 5: Puzzle 9 of 10

Can you figure out what number to replace the 25 with to
draw a circle?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level32')
artist.speed = 'fastest'

a = artist
for count in range(360):                          # ???
    a.move_forward(1)
    a.turn_right(1)

a.check()
