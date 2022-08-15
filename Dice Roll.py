# Imports
from PySimpleGUI import *

# Variables
result = 0


# The func to roll the dice
def roll(output):
    output = random.randrange(1, 7)
    return output


# The func to match the dice roll with the image path
def match(dice: int):
    match dice:
        case 1:
            return "Dice-1.png"
        case 2:
            return "Dice-2.png"
        case 3:
            return "Dice-3.png"
        case 4:
            return "Dice-4.png"
        case 5:
            return "Dice-5.png"
        case 6:
            return "Dice-6.png"
        case default:
            return "not working"


# The layout
Main_layout = [
    [Text(key="-RESULT-")],
    [Button("Roll Dice")]
]

Dice_image_layout = [
    [Text("The dice roll in an image")],
    [Image(key='-IMAGE-')]
]
layout = [
    [Column(Main_layout)],
    [HSeparator()],
    [Column(Dice_image_layout)]
]

# The window
window = Window(title="Dice Roll", layout=layout, size=(500, 500))

# The event loop
while True:
    event, values = window.read()
    if event == "Roll Dice":
        result = roll(result)
        window['-RESULT-'].update(str(result))
        window['-IMAGE-'].update(match(int(result)))

    elif event == WIN_CLOSED:
        break

# End program if user closes window or
window.close()
