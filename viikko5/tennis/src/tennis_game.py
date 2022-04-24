class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Forty-All"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.even()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.win()
        else:
            return self.match()

    def match(self):
        return self.scores[self.m_score1].split("-")[0] + "-" + self.scores[self.m_score2].split("-")[0]

    def win(self):
        diff = self.m_score1 - self.m_score2
        if diff == 1:
            return "Advantage " + self.player1_name
        elif diff == -1:
            return "Advantage " + self.player2_name
        elif diff >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def even(self):
        return self.scores[self.m_score1] if self.m_score1 in self.scores.keys() else "Deuce"
