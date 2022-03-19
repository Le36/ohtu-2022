class Player:
    def __init__(self, name, nat, ass, goa, pena, team, game):
        self.name = name
        self.nat = nat
        self.ass = ass
        self.goa = goa
        self.pena = pena
        self.team = team
        self.game = game

    def __str__(self):
        return f"{self.name:20}"
