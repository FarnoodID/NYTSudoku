# NYTSudoku

A simple Python program designed to solve [Sudoku puzzles](https://www.nytimes.com/puzzles/sudoku). This repository provides a simple command-line interface for users to input a Sudoku puzzle and receive the solved board as output.

## NYT Puzzles and codes
| Puzzles        | Code       |
|----------------|----------------|
| [Wordle](https://www.nytimes.com/games/wordle/index.html)    | [NYTWordle](https://github.com/FarnoodID/NYTWordle)           |
| [Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) | [NYTLetterBoxed](https://github.com/FarnoodID/NYTLetterBoxed) |
| [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) | [NYTSpellingBee](https://github.com/FarnoodID/NYTSpellingBee) |
| [Sudoku](https://www.nytimes.com/puzzles/sudoku)             | NYTSudoku          |
| [Pixletters](https://pixletters.com/)                        | [Pixletters](https://github.com/FarnoodID/Pixletters)         |

## Overview

Sudoku is a logic-based number-placement puzzle where the goal is to fill a 9×9 grid so that each column, each row, and each of the nine 3×3 subgrids contain all digits from 1 to 9. **NYTSudoku** utilizes a backtracking algorithm to solve these puzzles efficiently.

## Features

- **User-Friendly Input**: Enter the Sudoku puzzle using zeroes for empty cells.
- **Backtracking Algorithm**: Efficiently solves the puzzle using backtracking techniques.
- **Validation Checks**: Ensures compliance with Sudoku rules during solving.
- **Visual Output**: Displays the solved Sudoku board in a clear format.

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of command-line operations

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/FarnoodID/NYTSudoku.git
   ```
2.  Run the program:
     ```bash
     pyhton NYTSudoku.py
     ```
    You will be prompted to enter your Sudoku puzzle. Input the numbers separated by spaces, using zeroes for empty boxes. For example:
    
    ```text
    0 9 0 0 3 0 8 5 0
    2 0 0 0 0 0 0 0 3
    0 0 0 0 5 0 2 0 0
    0 4 0 7 9 3 0 0 0
    0 5 0 0 2 0 0 0 0
    6 0 9 0 0 0 0 3 0
    0 0 0 0 0 9 4 8 0
    0 0 0 0 8 0 0 1 0
    8 0 7 5 4 0 0 0 0
    ```
