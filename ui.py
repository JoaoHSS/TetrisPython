import pygame as pg

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pg.display.set_mode((width, height))
        
    def draw_board(self, board, offset=150):
        for i, row in enumerate(board.grid):
            for j, cell in enumerate(row):
                pg.draw.rect(self.window, cell.color,
                            (j*cell.size+offset, i*cell.size, cell.size,cell.size))
                pg.draw.rect(self.window, (50,50,50), 
                            (j*cell.size+offset, i*cell.size, cell.size,cell.size), 1)
    
    def draw_current_piece(self, piece, offset=150):
        for line in piece.shape:
            for cell in line:
                if cell.empty:
                    continue
                pg.draw.rect(self.window, cell.color,
                            (cell.x*cell.size+offset, cell.y*cell.size, cell.size,cell.size))
                pg.draw.rect(self.window, (50,50,50), 
                            (cell.x*cell.size+offset, cell.y*cell.size, cell.size,cell.size), 1)
    
    def draw_hold(self, hold):
        if hold == None:
            return
        for line in hold.shape:
            for cell in line:
                if cell.empty:
                    continue
                pg.draw.rect(self.window, cell.color,
                            (cell.x*cell.size, cell.y*cell.size, cell.size,cell.size))
                pg.draw.rect(self.window, (50,50,50), 
                            (cell.x*cell.size, cell.y*cell.size, cell.size,cell.size), 1)

    def draw_previews(self, pieces_list, indx):
        for n in range(5):
            piece = pieces_list[indx+n]
            for i, line in enumerate(piece.shape):
                for j, cell in enumerate(line):
                    pg.draw.rect(self.window, cell.color,
                                (275+150+j*25, 25+n*75+i*25, cell.size, cell.size))

    def draw_score(self, score):
        font = pg.font.Font('freesansbold.ttf', 16)
        text = font.render(str(score), True, (255,255,255))
        textRect = text.get_rect()
        textRect.topleft = (0,0)
        self.window.blit(text, textRect)

    def draw_game_over_screen(self, score):
        font = pg.font.Font('freesansbold.ttf', 50)
        text = font.render("FIM DE JOGO", True, (255,255,255))
        text2 = font.render(f"score: {score}", True, (255,255,255))
        textRect = text.get_rect()
        text2Rect = text2.get_rect()
        textRect.center = (self.width//2, self.height//2)
        text2Rect.center = (self.width//2, self.height//2+50)
        self.window.blit(text, textRect)
        self.window.blit(text2, text2Rect)
    
    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                return True
        return False