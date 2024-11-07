#!/usr/bin/python3
""" nqueens problem """
import sys


def solve(row, size, columns, positive_diagonals, negative_diagonals, chessboard):
  """ backtrack to find solution """
  if row == size:
    result = []
    for i in range(len(chessboard)):
      for j in range(len(chessboard[i])):
        if chessboard[i][j] == 1:
          result.append([i, j])
    print(result)
    return

  for col in range(size):
    if col in columns or (row + col) in positive_diagonals or (row - col) in negative_diagonals:
      continue

    columns.add(col)
    positive_diagonals.add(row + col)
    negative_diagonals.add(row - col)
    chessboard[row][col] = 1

    solve(row + 1, size, columns, positive_diagonals, negative_diagonals, chessboard)

    columns.remove(col)
    positive_diagonals.remove(row + col)
    negative_diagonals.remove(row - col)
    chessboard[row][col] = 0


def nqueens(size):
  """ Solution of nqueens """
  columns = set()
  positive_diagonals = set()
  negative_diagonals = set()
  chessboard = [[0] * size for _ in range(size)]

  solve(0, size, columns, positive_diagonals, negative_diagonals, chessboard)


if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
  try:
    i = int(args[1])
    if i < 4:
      print("N must be at least 4")
      sys.exit(1)
    nqueens(i)
  except ValueError:
    print("N must be a number")
    sys.exit(1)
