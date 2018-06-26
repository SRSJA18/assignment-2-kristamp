# Please reference the included PDF for complete instructions.
#
# You can create your table (from the instructions) using a doc or spreadsheet.
#
# Advanced students should attempt to implement
# Rock, Paper, Scissors, Lizard, Spock using 3 or 4 players instead (This is much harder.)
# 1. Ask player 1 for their move.
p1= input ("p1 enter your move ")
# 2. Check if player 1's move is valid.

# 3. Ask player 2 for their move.
p2= input ("p2 enter your move ")
# 4. Check if player 1's move is valid.

# 5. Print out the winner or 'tie'


if p1==p2:
    print ("tie")
elif p1=="rock":
    if p2=="paper":
        print ("p2")
    else:
        print ("p1")
elif p1=="paper":
    if p2=="scissors":
        print ("p2")
    else:
        print ("p1")
elif p1=="scissors":
    if p2=="rock":
        print ("p2")
    else:
        print ("p1")