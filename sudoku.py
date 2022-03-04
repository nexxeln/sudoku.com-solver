import time
import sys
import numpy as np
import pyautogui as pg


class SudokuSolver:
    def __init__(self) -> None:
        # initialize grid
        self.grid = np.array(np.zeros((9, 9)))
        self._take_input()

    def _take_input(self):
        row_number = 1

        while True:
            row = list(input("Enter the row: "))
            ints = [int(n) for n in row if n.isdigit()]

            if len(ints) != 9:
                print("Invalid input, please try again")
                continue

            for i in ints:
                self.grid[row_number - 1][ints.index(i)] = i
            print(f"Row {row_number} filled")

            if row_number == 9:
                print("All grids filled, solving...")
                break
            row_number += 1

    def _fill(self, matrix):
        """
        fills the grid with the numbers in the matrix
        """
        print("Filling the grid")
        final = [i for i in matrix.flatten()]

        counter = []

        for num in final:
            pg.typewrite(str(int(num)))
            pg.hotkey("right")
            counter.append(num)
            if len(counter) % 9 == 0:
                pg.hotkey("down")
                for _ in range(9):
                    pg.hotkey("left")         

    def _possible(self, x, y, n):
        """
        checks if the number n is possible in the given row, column, and 3x3 square
        """
        # check row
        for i in range(0, 9):
            if self.grid[i][x] == n and i != y:
                return False

        # check column
        for i in range(0, 9):
            if self.grid[y][i] == n and i != x:
                return False

        # check 3x3 square
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for X in range(x0, x0 + 3):
            for Y in range(y0, y0 + 3):
                if self.grid[Y][X] == n:
                    return False

        return True

    def solve(self):
        """
        solves the sudoku using backtracking
        """
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self._possible(x, y, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
                    
        self._fill(self.grid)
        print("Solved!")
        sys.exit()


if __name__ == "__main__":
    solver = SudokuSolver()
    time.sleep(5)
    print("Solving...")
    solver.solve()
