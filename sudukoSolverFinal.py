import math
import copy

# A Utility Function to print the Grid 
def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j],end=' ') 
        print ('n')

def getCoordinate(square, row, col):
    r1 = int(row - row%square)
    r2 = int(r1 + square - 1)
    c1 = int(col - col%square)
    c2 = int(c1 + square - 1)
    return (r1,r2),(c1,c2)

def find_next(arr,i,j):
    for x in range(i, len(arr)):
        for y in range(j, len(arr)):
            if(arr[x][y] == 0):
                return x, y
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            if(arr[x][y] == 0):
                return x, y
    return -1, -1

def valid_list(arr, size, square, row, col):
    validList = set()
    x, y = getCoordinate(square, row, col)
    for i in range(size):
        try:
            validList.add(arr[row][i])
            validList.add(arr[i][col])
        except:
            pass
    for j in range(x[0],x[1]+1):
        for k in range(y[0],y[1]+1):
            try:
                validList.add(arr[j][k])
            except:
                pass            
    validList.discard(0)
    return list(set(range(1,size+1)).difference(validList))
    

def solve_sudoku(arr, size, square, row=0, col=0):
    row, col = find_next(arr, row, col)
    if row == -1:
        return True
    for num in valid_list(arr, size, square, row, col):
        arr[row][col] = num
        if solve_sudoku(arr, size, square, row, col):
            return True
        arr[row][col] = 0
    return False

def solve(dataArray):
    if(solve_sudoku(dataArray, len(dataArray), math.sqrt(len(dataArray)))):
        return True
    else:
        return False


# Driver main function to test above functions 
if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid =[[0 for x in range(9)]for y in range(9)] 
      
    # assigning values to the grid 
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 
    tempGrid = copy.deepcopy(grid)
    size = len(tempGrid)
    square = math.sqrt(size)
    # if success print the grid 
    if(solve_sudoku(tempGrid, size, square)):
        print_grid(grid)
        print()
        print_grid(tempGrid) 
    else: 
        print("No solution exists")
