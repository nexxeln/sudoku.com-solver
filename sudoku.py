# imports
import pyautogui as pg 
import time

# initialize grid
grid = []

# input the rows of the grid
while True:
    row = list(input("Row: "))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        print("Row 9 complete")
        break
    print(f"Row {str(len(grid))} complete")

# give the user a few seconds to click on the initial square
time.sleep(10)

def possible(x, y, n):
    """
    checks if the number n is possible in the given row, column, and 3x3 square
    """
    # check row
    for i in range(0, 9):
        if grid[i][x] == n and i != y: 
            return False

    # check column
    for i in range(0, 9):
        if grid[y][i] == n and i != x: 
            return False

    # check 3x3 square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  
            if grid[Y][X] == n:
                return False    
    return True

def fill(matrix):
    """
    fills the grid with the numbers in the matrix
    """
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey("right")
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey("down")
            for _ in range(8):
                pg.hotkey("left")



def solve():
    """
    solves the sudoku using backtracking
    """
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    fill(grid)
    input("Solved")

if __name__ == "__main__":
    # solve the sudoku
    solve()