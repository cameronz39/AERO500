class SportsTeam():
    def __init__(self, teamName, players, coaches, power_rating):
        self.name = teamName
        self.players = players
        self.coaches = coaches
        self.power_rating = power_rating

    def startingLineup(self):
        return self.players
    
    def league_ranking(self):
        return self.power_rating
    
    def __len__(self) -> int:
        return len(self.players)
    
    def __str__(self):
        return f"Sports team: {self.name} with {len(self.players)} players"
 
    def __lt__(self, otherTeam: object):
        return self.power_rating < otherTeam.power_rating
    
    def __gt__(self, otherTeam: object):
        return self.power_rating > otherTeam.power_rating


class BasketballTeam(SportsTeam):
    def __init__(self, teamName, players, coaches, power_rating):
        super().__init__(teamName, players, coaches, power_rating)
        self.threes_made = 0
        self.threes_attempted = 0

    def startingLineup(self):
        return self.players[:5]
    
    def league_ranking(self):
        return int(round(1 + (self.power_rating/2400)*29))
    
    def get_three_point_percentage(self):
        if self.threes_attempted == 0: 
            return 0
        return 100 * self.threes_made / self.threes_attempted
    
    def __str__(self):
        return f"{self.name} (Basketball)"

    
class SoccerTeam(SportsTeam):
    def __init__(self, teamName, players, coaches, power_rating):
        super().__init__(teamName, players, coaches, power_rating)
        self.goals_for = 0
        self.goals_against = 0

    def startingLineup(self):
        return self.players[:11]
    
    def league_ranking(self):
        return int(round(1 + (self.power_rating/2400)*47))
    
    def get_goal_difference(self):
        return self.goals_for - self.goals_against

    def __str__(self):
        return f"{self.name} (Soccer)"
    
    