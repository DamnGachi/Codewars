def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name