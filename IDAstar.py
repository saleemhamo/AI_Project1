import random
from state import State
import numpy as np
import matplotlib.pyplot as plt
from PriorityQueue import PriorityQueue
from collections import deque

cutoff_values = []
next_cutoff = 0
path_queue = deque()
possible_next_states = PriorityQueue()
least_cutoff = 0
cutoff = 0
parent = None


def add_sorted_to_queue(list_of_states):
	global possible_next_states
	for i in range(0, len(list_of_states)):
		item = possible_next_states.find(list_of_states[i])
		if item == None:
			possible_next_states.enqueue(list_of_states[i])
		else:
			if int(item.total_cost) > int(list_of_states[i].total_cost):
				possible_next_states.delete(item)
				possible_next_states.enqueue(list_of_states[i])


def plot_board(state, title, name, n):
	board = np.zeros((n, n))
	board[1::2, 0::2] = 1
	board[0::2, 1::2] = 1

	for i in range(0, n):
		board[state.queens[i]][i] = 4

	b = plt.imshow(board, cmap='binary')
	plt.title(title)
	plt.savefig("./images/{}.png".format(name))
	# plt.show()


def save_states():
	global n
	global path_queue
	path_length = len(path_queue)
	for i in range(1, path_length+1):
		state = path_queue.popleft()
		plot_board(state, "State - {}".format(i), "{}".format(i), n)


def generate_next_states(current):
	next_states = []
	queens = current.queens
	for i in range(0, len(current.queens)):
		current_queens = queens.copy()
		current_queens = current.queens
		for j in range(0, len(current_queens)):
			next_queens = current_queens.copy()
			if current_queens[i] != j:
				next_queens[i] = j
				if parent != None:
					if next_queens == parent.queens:
						continue

				# print("Generate: {}".format(next_queens))
				generated_state = State(next_queens, current, abs(current_queens[i] - j))
				next_states.append(generated_state)
	return next_states


def is_goal(current_state):
	if current_state.heuristic == 0:
		return True
	else:
		return False


def solution(initial_state):
	global next_cutoff
	next_cutoff = 0
	global cutoff_values
	cutoff_values.clear()
	global possible_next_states
	global cutoff
	possible_next_states.enqueue(initial_state)
	goal = None
	while goal == None:

		cutoff = next_cutoff
		cutoff_values.append(cutoff)
		# cutoff = cutoff_queue.popleft()
		# cutoff = int(possible_next_states.dequeue().total_cost)

		goal = IDAstar(initial_state, 0)


	return goal


counter = 0


def IDAstar(current_state, counter):
	global path_queue
	global n
	counter += 1
	max_count = counter
	global next_cutoff
	global cutoff


	if current_state.total_cost > cutoff:
		# cutoff_queue.append(current_state.total_cost)
		next_cutoff = current_state.total_cost
		return None
	if is_goal(current_state):
		return current_state

	list_of_next_states = generate_next_states(current_state)
	list_of_next_states.sort(key=lambda x: x.total_cost, reverse=True)

	for i in range(0, len(list_of_next_states)):
		next_ = IDAstar(list_of_next_states[i], counter)
		if next_ != None:
			path_queue.append(list_of_next_states[i])
			counter -= 1
			return next_
	return None


def generate_initial_state(n):
	inital_queens = []
	for i in range(0, n):
		inital_queens.append(random.randint(0, n - 1))

	# print(inital_queens)
	return inital_queens

#
#
# a = [1, 5, 3, 4, 0]
# a.sort(key=None, reverse=False)
# print(a)
# #
# n = 4
# initial_state = State(generate_initial_state(n), 0, 0)
# possible_next_states.enqueue(initial_state)
#
# plot_board(initial_state, "Initial State", "initial_state", n)
# sol = solution(initial_state)
# plot_board(sol, "Goal State", "Goal_state", n)
#
#
# # save_states()
# #


#


# _______________________________________________________________________________________________


# def find_goal(initial_state):
# 	global queue
# 	global cutoff
# 	goal_state = None
# 	while goal_state == None:
# 		queue.clear_queue()
# 		queue.enqueue(State(initial_state, 0, 0))
# 		current = queue.dequeue()
# 		if is_goal(current):
# 			goal_state = current
# 			break
# 		while (is_goal(current) == False) & (current.total_cost <= cutoff):
# 			current.next_states = generate_next_states(current)
#
# 			# add_sorted_to_queue(current.next_states)  # no duplication
#
# 			try:
# 				current = queue.dequeue()
# 			except(Exception):
# 				print("Empty queue")
#
# 		if is_goal(current):
# 			goal_state = current
# 			break
# 		cutoff = current.total_cost
# 	return goal_state
#
