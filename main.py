import pygame
from src.setting import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from src.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    
    game = Game(screen)
    game.run(clock, FPS)

if __name__ == "__main__":
    main()