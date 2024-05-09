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
    
    def run_line(self, line:int, num:str) -> None:
        for element in self.sudoku[line]:
            if num == element:
                return True
        return False

    def run_col(self, column:int, num:str) -> None:
        for l in range(0,9):
            element = self.sudoku[l][column]
            if num == element:
                return True
        return False

    def run_box(self, a:int, b:int, c:int, d:int, num:str) -> None:
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
        for linha in range(a,b):
            for coluna in range(c,d):
                element = self.sudoku[linha][coluna]
                if num == element:
                    return True
            return False

    def find_occr(self, num:str):
        founded_line = self.run_line(0, num)
        founded_column = self.run_col(2, num)
        founded_box = self.run_box(0,3,0,3, num)
        
        if(founded_box or founded_column or founded_line): return True
        return False
      

sudokuSolve = SudokuSolve()

print(sudokuSolve.find_occr("6"))
