irl = 50
dem = 15


# irl = 1 min == 60 sec
# dem = 1 min == 600 sec


def normal_time(irl, dem):
    # Подсчет времени если бы было все нормально
    return (irl * 60 + dem * 600) / 3600
    # Result = 3.3333333333333335


def idiot_time(irl, dem):
    return (irl * 600 + dem * 600) / 3600
    # Result = 10.833333333333334


print(normal_time(irl, dem))
print(idiot_time(irl, dem))
