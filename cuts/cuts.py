import pyagg
from random import *
import time
import sys


# Utility to figure out how to cut lengths.  I needed this when cutting doors, and needed to figure out how
# to best utlitize lengths of wood of varying sizes.  This simply randomly looks for solutions until it
# finds one.  It is not guaranteed to find an optimal solution (and if there is no solution will just run 
# forever)


# Need to get as inputs:
# The lengths of the boards to cut
# The lengths of the boards needed
# Display preferences?
# Space to leave for cutting
# Filename to save (if any) 

#usage 
# needed=3,3,3,3
# have=3,3,3,3
# blade_width=4
# filename=test.png

board_colors = [ (255,248,220), (218,165,32), (244,164,96), (210,180,140), (222,184,135), (245,222,179), (255,222,173) ]

class wood:
    def __init__(self, l):
        self.length = l
        self.orig_length = l
        self.pieces = []


def cut_boards():
    lengths = [72,72,62,60.5,60,60.5,60,60.5,60,60,60.5,53,49.5,49.5,48,48,48,48,48,48]

    boards = []
    boards_needed=[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,23.25,23.25,23.25,23.25,23.25,23.25,23.25,23.25,50.75,50.75,50.75,50.75,50.75,50.75,50.75,50.75]
    
    for length in lengths:
        boards.append(wood(length))
    
    
    while len(boards_needed) != 0:
        b = randint(0,len(boards_needed) - 1)
        board_to_place = boards_needed.pop(b)
        counter=0
        while board_to_place:
            x = randint(0, len(boards) - 1)
            potential_fit = boards[x]
            if (board_to_place + .5) < potential_fit.length:
                potential_fit.length = potential_fit.length - (board_to_place + .5)
                potential_fit.pieces.append(board_to_place)
                board_to_place=None
            else:
                counter = counter + 1
            if counter > 200:
                return False
    return boards

def draw_solution(boards):
    length_multiplier = 10
    height = 20
    space_between = 35

    canvas_height = len(boards) * (height + space_between)
    canvas = pyagg.Canvas("210mm", str(canvas_height) + "px", background=(222,222,222), ppi=96)
    #canvas = pyagg.Canvas("210mm", "297mm", background=(222,222,222), ppi=96)

    number = 0
    for b in boards:
        # Draw the main board
        x = 10
        y = number * space_between + space_between
        x1 = 10 + length_multiplier * b.orig_length
        y1 = space_between * number + height
    
        canvas.draw_box(bbox=[x,y,x1,y1],
                        fillcolor=(139,69,19))
    
        number = number + 1
        canvas.draw_text(str(b.orig_length) + "\"",
                        xy=(x1 + 5, (y + y1) / 2),
                        anchor="w",
                        textsize=16)
    
        # Draw the pieces
        left = x
        for piece in b.pieces:
            right = left + piece * length_multiplier
            color = board_colors[ randint(0, len(board_colors)-1)  ]
            canvas.draw_box(bbox=[left,y,right,y1],
                            fillcolor=color)
            canvas.draw_text(str(piece) + "\"",
                            xy=( ( (left + right) / 2), y - (height / 2) ),
                            justify="left",
                            textsize=16)
            left = right
    
    
    
    canvas.save("test.png")
    canvas.view()



boards = False
while boards == False:
    boards = cut_boards()

draw_solution(boards)


