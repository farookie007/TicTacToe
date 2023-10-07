import time
from typing import List


class TicTacToe:
	def __init__(self):
		self.board = [" " for _ in range(9)]  # we will use a single list to repr the 3x3 board
		self.current_winner = None  # keep track of winner

	def print_board(self):
		for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	@staticmethod
	def print_board_number():
		number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
		for row in number_board:
			print('| ' + ' | '.join(row) + ' |')

	@property
	def available_moves(self) -> List:
		return [i for i, spot in enumerate(self.board) if spot == " "]

	@property
	def empty_squares(self):
		return bool(self.available_moves)

	@property
	def num_of_empty_squares(self) -> int:
		return self.board.count(" ")

	def make_move(self, square, letter):
		if self.board[square] == ' ':
			self.board[square] = letter
			if self.win(square, letter):
				self.current_winner = letter
			return True
		return False

	def win(self, square, letter):
		row_index = square // 3
		row = self.board[row_index*3:(row_index+1)*3]
		if all([spot == letter for spot in row]):
			return True

		col_index = square % 3
		column = [self.board[col_index+(i*3)] for i in range(3)]
		if all([spot == letter for spot in column]):
			return True

		if square % 2 == 0:
			diagonal_1 = [self.board[i] for i in [0, 4, 8]]
			if all([spot == letter for spot in diagonal_1]):
				return True
			diagonal_2 = [self.board[i] for i in [2, 4, 6]]
			if all([spot == letter for spot in diagonal_2]):
				return True
		return False


def play(game, x_player, o_player, print_game=True):
	if print_game:
		game.print_board_number()
	letter = 'X'
	square = None
	while game.empty_squares:
		if letter == 'O':
			square = o_player.get_move(game)
		if letter == 'X':
			square = x_player.get_move(game)

		if game.make_move(square, letter):
			if print_game:
				print(f"{letter} makes a move to square {square}")
				game.print_board()
				print()

			if game.current_winner:
				if print_game:
					print(f"{letter} wins!")
				return letter
			letter = 'O' if letter == 'X' else 'X'
		if print_game:
			time.sleep(1)
	if print_game:
		print("It's a Tie!!!")
		return
