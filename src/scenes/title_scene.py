import pygame
from src.scenes.base_scene import BaseScene
from src.setting import WHITE, BLACK

class TitleScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 40)
        self.title_text = self.font.render("PoKemon Volly", True, WHITE)

    def handle_events(self, events):
        """이벤트 처리 """
        

    def update(self, dt):
        """상태 갱신"""
        
    def draw(self, screen):
        """화면 구성"""
        screen.fill(BLACK)
        screen.blit(self.title_text, (200, 150))