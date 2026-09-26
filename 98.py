#98 Write a python program to Find the key with maximum value  a dictionary.
scores = {"player1": 150, "player2": 340, "player3": 210}
top_player_key = max(scores, key=scores.get)
print("Identified dictionary key carrying largest metric:", top_player_key)
