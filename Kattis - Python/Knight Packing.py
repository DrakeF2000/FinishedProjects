# Problem is kind of like tic tac toe but different - in tic tac toe first person to move is the only one who ever has the chance to win depending on where they place it - placement does
# not matter here as the winner is already predetermined by the size of the board and whether they move first or second - to explain the simplicity of the code
intialInput = int(input())
if intialInput % 2 == 1:
    print("first")
else:
    print("second")