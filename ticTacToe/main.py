from game import Game

game = Game()

while game.game_is_on and len(game.played_positions) < 9:
    print(game.game_board)
    game.play_move()

print(game.game_board)
print("------------------------------------------GAME OVER------------------------------------------------------")