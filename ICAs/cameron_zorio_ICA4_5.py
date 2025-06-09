from ICAs.sports_teams import BasketballTeam, SoccerTeam

warriors = BasketballTeam(
    "Golden State Warriors",
    players = ["Curry", "Green", "Kuminga", "Butler", "Hield", "Looney"],
    coaches = ["Kerr"],
    power_rating = 1800
)

barca = SoccerTeam(
    "FC Barcelona",
    players=[
        "Ter Stegen", "Araujo", "Kounde", "Christensen", "Balde",
        "Pedri", "De Jong", "Gündoğan", "Yamal", "Lewandowski",
        "Raphinha", "Ferran"
    ],
    coaches=["Xavi"],
    power_rating = 1910
)

print("----------------------")
print(warriors)
print("Number of players: ", len(warriors))
warriors.threes_attempted += 10
warriors.threes_made += 6
print("3-pt percentage: ", warriors.get_three_point_percentage(), "%")
print("Starting lineup: ", warriors.startingLineup())

print("----------------------")
print(barca)
print("Number of players: ", len(barca))
barca.goals_for += 15
barca.goals_against += 11
print("Goal difference: ", barca.get_goal_difference())
print("Starting lineup: ", barca.startingLineup())

print("----------------------")
if warriors > barca:
    print(warriors, "rank above", barca)
else:
    print(barca, "ranks above", warriors)
