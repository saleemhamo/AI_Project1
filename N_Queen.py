def check_queens(cols):
	board = number_of_conflicts(cols)
	for i in range(0, len(cols)):
		if board[i][cols[i]] != 0:
			return False
	return True


def number_of_conflicts(current_state):
	n = len(current_state)

	# create board
	board = {}
	for i in range(0, n):
		board[i] = list({})
		for k in range(0, n):
			board[i].append(0)

	# conflicts from the same row
	for i in range(0, n):
		row = current_state[i]
		for j in range(0, n):
			if j == i:
				continue
			board[j][row] += 1

	# conflicts from the same column
	for i in range(0, n):
		col = i
		for j in range(0, n):
			if j == current_state[i]:
				continue
			board[col][j] += 1

	# conflicts from the same diagonal
	for i in range(0, n):
		if i >= current_state[i]:
			row = 0
		else:
			row = current_state[i] - i
		if i <= current_state[i]:
			col = 0
		else:
			col = i - current_state[i]

		while (0 <= row) & (row < n) & (0 <= col) & (col < n):
			if row == current_state[i]:
				row += 1
				col += 1
				continue
			board[col][row] += 1
			row += 1
			col += 1
	for i in range(0, n):

		if (n - 1) >= current_state[i] + i:
			col = 0
		else:
			col = current_state[i] - ((n - 1) - i)

		if (n - 1) <= current_state[i] + i:
			row = (n - 1)
		else:
			row = i + current_state[i]


		while (n > row) & (row >= 0) & (0 <= col) & (col < n):
			if row == current_state[i]:
				row -= 1
				col += 1
				continue
			board[col][row] += 1
			row -= 1
			col += 1



	return board


def print_board(board, current_state):
	for row in range(0, len(board)):
		for column in range(0, len(board)):
			if current_state[column] == row:
				print("Q{}    ".format(column), end=" ")
			else:
				print("{:<2}    ".format(board[column][row]), end=" ")
		print("\n")


def print_board2(board, current_state):
	for row in range(0, len(board)):
		for column in range(0, len(board)):
			print("{:<2}    ".format(board[column][row]), end=" ")
		# if current_state[column] == row:
		# 	print("Q{}    ".format(column), end=" ")
		# else:
		# 	print("{:<2}    ".format(board[column][row]), end=" ")
		print("\n")


