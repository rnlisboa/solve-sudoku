from random import randint
sudoku = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

class SudokuSolve:
    sudoku = sudoku

    def print_sudoku(self) -> None:
        for lines in self.sudoku:
            print(lines)
    
    def run_line(self, line:int, num:str) -> bool:
        for element in self.sudoku[line]:
            if num == element:
                return True
        return False

    def run_col(self, column:int, num:str) -> bool:
        for l in range(0,9):
            element = self.sudoku[l][column]
            if num == element:
                return True
        return False

    def run_box(self, l:int, c:int, num:str) -> bool:
        # PARA EVITAR ESSES PARAMETROS, PRECISO SABER ONDE O CURSOR ESTÁ NA MATRIZ
        """
          l     c
        [0,3] [0,3]---- primeira caixa da primeira linha
        [0,3] [3,6]---- segunda caixa da primeira linha  
        [0,3] [6,9]---- terceira caixa da primeira linha

        [3,6] [0,3]---- primeira caixa da segunda linha
        [3,6] [3,6]---- segunda caixa da segunda linha
        [3,6] [6,9]---- terceira caixa da segunda linha

        [6,9] [0,3]---- primeira caixa da terceira linha
        [6,9] [3,6]---- segunda caixa da terceira linha
        [6,9] [6,9]---- terceira caixa da terceira linha

        """

        # os parametros da função devera ser os os limites a,b e c,d para linha e coluna
        a, b, c, d = 0,3,0,3
        for linha in range(a,b):
            for coluna in range(c,d):
                element = self.sudoku[linha][coluna]
                if num == element:
                    return True
        return False

    def find_occr(self, num:str, l:int, c:int) -> bool:
        founded_line = self.run_line(0, num)
        founded_column = self.run_col(2, num)
        founded_box = self.run_box(l,c, num)
        
        if(founded_box or founded_column or founded_line): 
            return True
        return False

    def run_matrix(self):
        for i in range(9):
            for j in range(9):
                case = self.sudoku[i][j]
                if case == '.':
                    num = randint(1,9)
                    can_set = self.find_occr(str(num), i, j)
      

sdkSolve = SudokuSolve()

sdkSolve.run_matrix()
