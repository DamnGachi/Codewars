import re


def who_is_winner(arr):
    res_yellow = []
    res_red = []
    if 'Red' in arr[0]:
        red = arr[::2]
        yellow = arr[1:][::2]
        red = ' '.join(red)[::6]
        yellow = ' '.join(yellow)[::9]
    if 'Yellow' in arr[0]:
        yellow = arr[::2]
        red = arr[1:][::2]
        red = ' '.join(red)[::6]
        yellow = ' '.join(yellow)[::9]


who_is_winner(arr=[
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
    "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
    "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
])
