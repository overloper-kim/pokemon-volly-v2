import pygame
from src.scenes.title_scene import TitleScene

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.current_scene = TitleScene(self) # 첫 세팅은 타이틀 화면

    def run(self, clock, fps):
        while self.running:
            dt = clock.tick(fps) / 1000

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.current_scene.handle_events(events)
            self.current_scene.update(dt)
            self.current_scene.draw(self.screen)

            pygame.display.flip()

    def change_scene(self, new_scene):
        self.current_scene = new_scene