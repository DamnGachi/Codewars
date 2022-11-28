# https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/python
def outed(meet, boss):
    boss_of_the_gym = meet.get(boss) * 2

    booss = meet.get(boss)

    dlina = len(meet.values())

    s = sum(meet.values()) - booss

    if (s + boss_of_the_gym) / dlina <= 5.0:
        return 'Get Out Now!'
    return 'Nice Work Champ!'
