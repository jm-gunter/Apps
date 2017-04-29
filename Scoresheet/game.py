class Game:
    """ A trivia game"""
    def __init__(self, teams, rounds, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self._teams = teams
        self._rounds = rounds
        self._scores = [[int() for r in range(self.rounds)] for t in range(self.teams)]
        self._totals = [int() for t in range(self.teams)]


    @property
    def teams(self):
        """Get or set the number of teams. Values must be of type int with value >0."""
        return self._teams

    @teams.setter
    def teams(self, number):
        if isinstance(number, int):
            if number > 0:
                self._teams = number
                self._scores = [[int() for r in range(self.rounds)] for t in range(self.teams)]
                self._totals = [int() for t in range(self.teams)]
            else:
                raise ValueError("Game must have at least one team.")
        else:
            raise ValueError("Rounds must be an integer")


    @property
    def rounds(self):
        """Get or set the number of rounds. Values must be of type int with value >0."""
        return self._rounds

    @rounds.setter
    def rounds(self, number):
        if isinstance(number, int):
            if number > 0:
                self._rounds = number
                self._scores = [[int() for r in range(self.rounds)] for t in range(self.teams)]
                self._totals = [int() for t in range(self.teams)]
            else:
                raise ValueError("Game must have at least one round.")
        else:
            raise ValueError("Rounds must be an integer")


    @property
    def scores(self):
        return self._scores

    def set_score(self, team, round, value):
        if isinstance(team, int) and isinstance(round, int) and isinstance(value, int):
            self._scores[team][round] = value
            self._totals[team] = 0
            for s in range(self.rounds):
                self._totals[team] += self._scores[team][s]
        else:
            raise ValueError("Arguments team, round, and value must be integers.")

    @property
    def team_totals(self):
        return self._totals
