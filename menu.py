from player.player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


INTRO = """Enter one of the following commands:
				'a': to play a versus game with a friend
				'b': to play with the computer [BEGINNER LEVEL]
				'c': to play with the computer [GENIUS LEVEL]
				
				Enter your choice: 
"""


def menu():
	print(INTRO)
	user_choice = input(">>> ")
	operations = {
		'a': HumanPlayer,
		'b': RandomComputerPlayer,
		'c': GeniusComputerPlayer
		}

	player_x = HumanPlayer('X')
	player_o = operations[user_choice]('O')
	return player_x, player_o
