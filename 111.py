class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1


for i in range(40):
    building = Buiding()
    print(Buiding.total)
