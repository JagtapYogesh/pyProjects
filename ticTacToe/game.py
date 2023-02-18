from data import game_board


class Game:
    def __init__(self):
        self.game_is_on = True
        self.is_x_next = True
        self.played_positions = []
        self.win_combinations = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {4, 5, 6}, {7, 8, 9}]
        self.game_board = game_board

    def play_move(self):
        player = 'X' if self.is_x_next else 'O'
        print(f"Player: {player}")
        position = int(input("Enter the position you want to play: "))
        if 9 >= position >= 1 and position not in self.played_positions:
            self.game_board = self.game_board.replace(str(position), player)
            self.played_positions.append(position)
            self.is_x_next = not self.is_x_next
            self.check_winner()
        else:
            print("Invalid position entered")

    def check_winner(self):
        if len(self.played_positions) >= 5:
            for index1 in range(0, len(self.played_positions)-4, 2):
                for index2 in range(index1+2, len(self.played_positions)-2, 2):
                    for index3 in range(index2+2, len(self.played_positions), 2):
                        is_winner_combination = {self.played_positions[index1], self.played_positions[index2], self.played_positions[index3]}
                        if is_winner_combination in self.win_combinations:
                            self.game_is_on = False
                            winner = 'X' if index1 % 2 == 0 else 'O'
                            print("###########################################################################################")
                            print(f"The winner is {winner}")
                            print("###########################################################################################")

            if len(self.played_positions) == 9 and self.game_is_on:
                self.game_is_on = False
                print("###########################################################################################")
                print("The game is drawn.")
                print("###########################################################################################")
