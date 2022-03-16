import unittest

from src.player import Player
from src.statistics import Statistics


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_top_scores(self):
        self.assertAlmostEqual(str(self.statistics.top_scorers(1)[0]), "Gretzky EDM 35 + 89 = 124")

    def test_team(self):
        self.assertAlmostEqual(str(self.statistics.team("PIT")[0]), "Lemieux PIT 45 + 54 = 99")

    def test_player(self):
        self.assertAlmostEqual(str(self.statistics.search("Kurri")), "Kurri EDM 37 + 53 = 90")
        self.assertIsNone(str(self.statistics.search("Nobody")))


if __name__ == '__main__':
    unittest.main()
