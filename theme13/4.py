class TeamIterator:
    def __init__(self, players):
        self.players = players
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.players):
            raise StopIteration

        player = self.players[self.index]
        self.index += 1

        return player


class Team:
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return TeamIterator(self.players)


team = Team(["Alex", "John", "Maria"])

for player in team:
    print(player)


for player in team:
    print(player)
