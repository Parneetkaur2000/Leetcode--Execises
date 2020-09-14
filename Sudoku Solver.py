Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

****************************************************************************************************

def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
         """
        # try to fill in the number
        def solve(board):
            
            find = find_empty(board)
            if not find:
                return True
            else:
                row, col = find
            
            for i in range(1,10):
                if valid(board,i,(row,col)):
                    board[row][col] = i
                    
                    if solve(board):
                        return True
                    
                    board[row][col] = 0
            return False
         
        def valid(board,num,pos):
            #check row
            for i in range(len(board[0])):
                if board[pos[0][i]] == num and pos[1] != i:
                    return False
            # check col
            for j in range(len(board)):
                if board[i][pos[1]] == num and pos[0] != i:
                    return False
            
            
            #check box
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            
            for i in range(box_y*3, box_y*3+3):
                for j in range(box_x*3, box_x*3 + 3):
                    if board[i][j] == num and (i,j) != pos:
                        return False
            return True
                
     #find the empty cell
        
        def find_empty(board):
            for i in range(len(board)):
                for j in range(len(board[0])):    #length of row
                    if board[i][j] == ' ':
                        return(i , j)
        return solve(board)
 
        
