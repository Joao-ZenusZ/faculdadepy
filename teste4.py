from random import randint


def partida(time1,time2):
    gol1 = randint(0, 5)
    golsofre1 = randint(0, 5)
    gol2 = randint(0, 5)
    golsofre2 = randint(0, 5)
    result1 = ((gol1 + golsofre2)/2)
    result2 = ((gol2 + golsofre1)/2)
    return f"{time1} {int(result1)} X {int(result2)} {time2}"
timecasa = input("Time da casa: ")
timefora = input("Time visitante: ")
num = " "
while num == " ":
    print(partida(timecasa, timefora))
    num = input("Continua:")