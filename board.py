from Piece import Block

class Board:
    def __init__(self, width, height, cellSize):
        self.width = width
        self.height = height
        self.grid = [[Block(i, j, (0,0,0),cellSize,1) for i in range(width)] for j in range(height)]
    
    def add_piece(self, piece):
        for line in piece:
            for cell in line:
                if cell.empty:
                    continue
                self.grid[cell.y][cell.x] = cell

