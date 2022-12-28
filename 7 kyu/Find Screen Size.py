def find_screen_height(width, ratio):
    s = ratio.split(':')[0]
    s1 = ratio.split(':')[1]
    return str(width) + 'x' + str(int(width / int(s) * int(s1)))
