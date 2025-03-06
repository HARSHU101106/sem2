players = [
    ("Messi", 7500),
    ("Ronaldo", 8200),
    ("Neymar", 3400),
    ("Mbappe", 5000),
    ("Lewandowski", 6100),
    ("Kane", 4600),
    ("Salah", 5300)
]

ascending_goals = sorted(players, key=lambda player: player[1])
print("\nPlayers sorted by goals (ascending order):", ascending_goals)

descending_goals = sorted(players, key=lambda player: player[1], reverse=True)
print("Players sorted by goals (descending order):", descending_goals)

top_3_scorers = descending_goals[:3]
print("Top 3 Goal Scorers:", top_3_scorers)

sorted_names = sorted(players, key=lambda player: player[0])
print("Players sorted by name (alphabetically):", sorted_names)

high_earners = list(filter(lambda player: player[1] > 5000, players))
print("Players who scored more than 5000 goals:", high_earners)
