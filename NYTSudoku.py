board = []
print("Put Sudoku with zeroes as empty boxes (space between each number)")
def get_board():
    for i in range (9):
        b=list(map(int,input().split()))
        board.append(b)

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        j=(i*3)%10+3
        if j>9:
            j-=9
        if valid(bo, j, (row, col)):
            bo[row][col] = j
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)
    return None

get_board()
solve(board)
print()
print_board(board)
input("Here You Are! ")