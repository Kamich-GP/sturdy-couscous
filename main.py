class Player:
    def __init__(self, power, speed, accuracy, stamina):
        self.power = power
        self.speed = speed
        self.accuracy = accuracy
        self.stamina = stamina


class GoalKeeper(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(power, speed, accuracy, stamina)

    def save(self):
        print('Поймал мяч')


class Striker(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(power, speed, accuracy, stamina)

    def goal(self):
        print('Забил мяч в ворота')
