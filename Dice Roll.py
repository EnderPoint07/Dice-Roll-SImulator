# Imports
from PySimpleGUI import *


# The func to roll the dice
def roll(output):
    output = random.randrange(1, 7)
    return output


# Variables
result = 0

# The layout
layout = [[Text("Press the button")], [Button("Roll Dice")]]

# The window
window = Window(title="Dice Roll", layout=layout)

# The event loop
while True:
    event, values = window.read()
    if event == "Roll Dice":
        print(str(roll(result)))
        layout = [[Text('You got the number: ' + str(roll(result)))], [Button("Roll Dice")]]
        window = Window(title="Dice Roll", layout=layout)

    elif event == WIN_CLOSED:
        break

# End program if user closes window or
window.close()
