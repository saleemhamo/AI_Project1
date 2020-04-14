from N_Queen import *


class State:
	def __init__(self, queens, parent, cost):
		if parent == None:
			self.path_cost = cost
		else:
			self.path_cost = parent.path_cost + cost

		self.heuristic = self.find_heuristic(queens)
		self.total_cost = self.path_cost + self.heuristic
		self.queens = queens
		self.next_states = []

	@staticmethod
	def find_heuristic(queens):
		"""sum of conflicts in queens positions"""
		current_board = number_of_conflicts(queens)
		heuristic = 0
		for i in range(0, len(queens)):
			heuristic += current_board[i][queens[i]]
		return heuristic
