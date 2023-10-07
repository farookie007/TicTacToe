from game.game import play, TicTacToe
from menu import menu

player_x, player_o = menu()

tictactoe = TicTacToe()

wins = {'X': 0, 'O': 0}
lives = 5
choice = input("Start Game [y/n]?: ")
while choice == 'y' and lives > 0:
    lives -= 1
    winner = play(tictactoe, player_x, player_o, print_game=True)
    if winner is not None:
        wins[winner] += 1
    o, x = wins['O'], wins['X']
    print(f"\n O - {o}".center(20))
    print(f"\n X - {x}".center(20))
    print(f"\n LIVES - {'o' * lives}".center(20))
    choice = input("Start Next Game [y/n]?: ")

    if lives == 0:
        print("You have no more lives left")

if x != o:
    print(f"The winner is {x if x>0 else o}!!!")
else:
    print("Tie!!!")
# END GAME
input("Press ANY KEY to end.")
