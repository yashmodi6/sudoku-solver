# sudoku-solver

A lightweight 9x9 Sudoku solver written in Python using backtracking search.

[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

## What it does

- Reads 81-character Sudoku strings from `puzzles.txt` (`0` denotes an empty cell).
- Solves each board using recursive backtracking against row, column, and 3x3 block constraints.
- Benchmarks against the 50-puzzle set from [Project Euler Problem 96](https://projecteuler.net/problem=96).
- Outputs the total execution time after completing the batch.

## Performance

### 1. Backtracking only

Solving times measured across 3 batch runs using `time.perf_counter()` on the 50 puzzles in `puzzles.txt`:

| Metric | Value |
| :--- | :---: |
| Total puzzles | 50 |
| Total batch time | 9.75 s |
| Average time per puzzle | 194.92 ms |
| Fastest puzzle | 0.37 ms |
| Slowest puzzle | 1.93 s |

## Usage

Solve a sample puzzle:

```bash
python sudoku.py
```

Run the benchmark suite:

```bash
python benchmarking.py
```

## License

This project is licensed under the [MIT License](LICENSE.md).
