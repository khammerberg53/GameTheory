import axelrod as axl

player1 = axl.TitForTat()
player2 = axl.Alternator()

match = axl.Match((player1, player2), turns = 6))
match.player()

match.final_score_per_turn()

