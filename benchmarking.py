import time

from sudoku import solve, text_to_sudoku


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
