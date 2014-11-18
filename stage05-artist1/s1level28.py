"""Stage 5: Puzzle 5 of 10

Now, for practice, draw a triangle and then a square to draw an envelope.
Hint: delete the 'pass' (which does nothing) with your code.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level28')

for count in range(3):
    artist.forward(100)
    artist.right(120)
    # ???
artist.right()

for count2 in range(4):
    artist.forward(100)
    artist.left()

artist.check()
