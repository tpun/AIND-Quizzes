from gamestate import *

print("Creating empty game board...")
g = GameState()

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print(p1_empty_moves)
print("")

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))
for p in g1.players:
    print(p)

print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
print(p2_empty_moves)
print("")

print("Applying move (1, 1) for player 2...")
g2 = g1.forecast_move((1,1))
for p in g2.players:
    print(p)

print("Getting legal moves for player 1...")
p1_empty_moves = g2.get_legal_moves()
print(p1_empty_moves)
