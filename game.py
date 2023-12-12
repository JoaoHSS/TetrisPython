import pygame as pg
from Piece import *

class Game:
    def __init__(self, board):
        self.board = board
        self.piece = None
        self.hold = None
        self.score = 0
        self.pieces_list = create_piece_list() + create_piece_list()
        self.piece_index = 0
        self.preview_piece = None
    
    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP6:
                self.moveside(1)
            
            if event.key == pg.K_KP4:
                self.moveside(-1)

            if event.key == pg.K_KP8:
                self.cwRotation()
            
            if event.key == pg.K_KP5:
                self.movedown()
            
            if event.key == pg.K_z:
                self.ccwRotation()

            if event.key == pg.K_c:
                self.holdPiece()   
            
            if event.key == pg.K_LCTRL:
                self.cwRotation()
                self.cwRotation()

            if event.key == pg.K_SPACE:
                while self.piece:
                    self.movedown()

    # a próxima peça da lista de peças se torna a atual, se a lista estiver no fim, gera mais peças
    def get_next_piece(self):
        if self.piece_index == 7:
            self.pieces_list = self.pieces_list[7:]
            self.pieces_list += create_piece_list()
            self.piece_index = 0
        
        self.piece = self.pieces_list[self.piece_index]
        self.piece_index += 1
    
    def holdPiece(self):
        if self.hold == None:
            self.hold = deepcopy(PIECES[self.piece.name])
            
            self.get_next_piece()
        else:
            self.piece, self.hold = deepcopy(PIECES[self.hold.name]), deepcopy(PIECES[self.piece.name])
        
        for line in self.hold.shape:
            for cell in line:
                cell.x -= 2
                cell.y += 1
        
    def moveside(self, side):
        for line in self.piece.shape:
            for cell in line:
                cell.x += side
        
        if not self.is_colliding():
            return
        
        for line in self.piece.shape:
            for cell in line:
                cell.x -= side

    def ccwRotation(self):
        
        n = len(self.piece.shape)

        rotated_matrix = [[None for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated_matrix[j][n-1-i] = [self.piece.shape[i][j].x, self.piece.shape[i][j].y]

        for j, line in enumerate(self.piece.shape):
            for i, cell in enumerate(line):
                cell.x, cell.y = rotated_matrix[j][i][0], rotated_matrix[j][i][1]
        
        if self.is_colliding():
            self.cwRotation()

    def cwRotation(self):
        
        n = len(self.piece.shape)

        rotated_matrix = [[None for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated_matrix[n-1-j][i] = [self.piece.shape[i][j].x, self.piece.shape[i][j].y]
                
        for j, line in enumerate(self.piece.shape):
            for i, cell in enumerate(line):
                cell.x, cell.y = rotated_matrix[j][i][0], rotated_matrix[j][i][1]    
        
        if self.is_colliding():
            self.ccwRotation()

    # move a peça para baixo, se estiver colodindo ou fora do tabuleiro, move para cima e fixa
    def movedown(self):
        for line in self.piece.shape:
            for cell in line:
                cell.y += 1
        
        if not self.is_colliding():
            return 
        
        for line in self.piece.shape:
            for cell in line:
                cell.y -= 1
        
        self.board.add_piece(self.piece.shape)
        self.piece = None

    def is_colliding(self):
        try:
            for line in self.piece.shape:
                for cell in line:
                    if cell.empty:
                        continue
                    if not self.board.grid[cell.y][cell.x].empty:
                        return True
                    if cell.x < 0:  # enconstar na parede esquerda
                        return True
        except IndexError:  # encostar na parede direita ou no chão
            return True

    def check_completed_rows(self):
        cleared = 0
        for indx, row in enumerate(self.board.grid):
            full = True
            for cell in row:
                if cell.empty:
                    full = False
                    break
            if full:
                cleared += 1
                top = [Block(0, n, (0,0,0), 25, 1) for n in range(10)]
                for indx_b, row_b in enumerate(self.board.grid[:indx+1]):
                    for cell_b in self.board.grid[indx_b]:
                        cell_b.y += 1
                    self.board.grid[indx_b] = top
                    top = row_b
        self.update_score(cleared)
    
    def update_score(self, num_completed_rows):
        # Update the score based on the number of completed rows
        self.score += num_completed_rows

    