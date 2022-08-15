# Imports
from PySimpleGUI import *

# Variables
result = 0


# The func to roll the dice
def roll(output):
    output = random.randrange(1, 7)
    return output


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# The func to match the dice roll with the image path
def match(dice: int):
    match dice:
        case 1:
            path = resource_path('images/Dice-1.png')
            return path
        case 2:
            path = resource_path('images/Dice-2.png')
            return path
        case 3:
            path = resource_path('images/Dice-3.png')
            return path
        case 4:
            path = resource_path('images/Dice-4.png')
            return path
        case 5:
            path = resource_path('images/Dice-5.png')
            return path
        case 6:
            path = resource_path('images/Dice-6.png')
            return path
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
