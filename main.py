import sys
import pygame as pg
from game import Game
from board import Board
from ui import UI

CELL_SIZE = 25
NUM_COLS = 10
NUM_ROWS = 20
WIDTH = NUM_COLS * CELL_SIZE + CELL_SIZE * 12
HEIGHT = NUM_ROWS * CELL_SIZE

def main():
    # inicializar pygame e criar objeto UI
    pg.init()
    pg.display.set_caption("Tetris")
    ui = UI(WIDTH, HEIGHT)
    fps = pg.time.Clock()

    # criar tabuleiro, jogo e peças
    board = Board(NUM_COLS, NUM_ROWS, CELL_SIZE)
    game = Game(board)
    
    # velocidade
    gravity = 30
    move_down = gravity
    game_over = False

    # começar loop do jogo
    while True:

        # atualizar a tela
        fps.tick(60)
        pg.display.update()
        ui.window.fill((0,0,0))

        # gerenciar eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if game.piece:
                game.handle_input(event)

            if ui.handle_event(event):
                board = Board(NUM_COLS, NUM_ROWS, CELL_SIZE)
                game = Game(board)
                game_over = False
        
        # virifica se é fim de jogo
        if game.piece:
            if game.is_colliding():
                game_over = True

        if game_over:
            game.piece = None
            ui.draw_game_over_screen(game.score)
            continue
        
        if game.piece:
            move_down -= 1
            
            if move_down == 0:
                game.movedown()
                move_down = gravity
            
        game.check_completed_rows()

        if game.piece == None:
            game.get_next_piece()

        # desenhar elementos do jogo na tela
        ui.draw_board(board)
        ui.draw_current_piece(game.piece)
        ui.draw_hold(game.hold)
        ui.draw_previews(game.pieces_list, game.piece_index)
        ui.draw_score(game.score)

if __name__ == "__main__":
    main()
