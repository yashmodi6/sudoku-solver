import time

type Sudoku = list[list[int]]


def text_to_sudoku(puzzle: str) -> Sudoku:

    if not puzzle.isdecimal():
        raise RuntimeError

    board: Sudoku = [[0] * 9 for _ in range(9)]

    for row, char in enumerate(puzzle):
        board[row // 9][row % 9] = int(char)
    return board


def print_sudoku(board: Sudoku) -> None:
    for row in board:
        print(*row)


def is_valid(board: Sudoku, row: int, col: int, num: int) -> bool:

    # Check for existing values in row and col
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # % gives the remainder after dividing by 3.
    # Subtracting that remainder moves us back to the nearest multiple of 3,
    # which is the starting row/column of the current 3x3 block.
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    # Check in 3*3 block
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True


def find_empty_cell(board: Sudoku) -> tuple[int, int] | None:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def solve(board: Sudoku) -> bool:
    blank = find_empty_cell(board)

    # If there are no empty cells left, the Sudoku is completely solved.
    if not blank:
        return True
    else:
        row, col = blank

    # Try every number from 1 to 9 in the empty cell.
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Temporarily place the valid number in the cell.
            board[row][col] = num

            # Recursively call solve() to solve the rest of the board.
            # The function keeps making recursive calls until:
            # 1. The board is completely solved, or
            # 2. The current choice leads to a dead end.
            if solve(board):
                return True

            # If the recursive call returns False, the number we chose
            # did not lead to a solution. Undo the choice by resetting
            # the cell to 0 and try the next possible number.
            board[row][col] = 0

    # If none of the numbers 1-9 work for this cell,
    # return False so the previous recursive call can backtrack.
    return False


def main() -> None:

    start = time.perf_counter()

    with open("puzzles.txt", "r", encoding="utf-8") as f:
        for line in f:
            puzzle_text = line.strip()

            if not puzzle_text:
                continue

            sudoku = text_to_sudoku(puzzle_text)

            solve(sudoku)

    end = time.perf_counter()
    print(f"Execution time: {end - start:.6f} seconds")


if __name__ == "__main__":
    main()
