import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            self.players.append(player)

        self.players.sort(key=lambda x: (int(x.goa) + int(x.ass)))
        self.players.reverse()


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, param):
        sort_players = []
        for player in self.reader.players:
            if player.nat == param:
                total = (int(player.goa) + int(player.ass))
                temp = f"{player.name:15}", "\t", player.team, " ", str(player.goa), " + ", str(player.ass), " = ", str(
                    total)
                sort_players.append("".join(temp))

        return sort_players


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
