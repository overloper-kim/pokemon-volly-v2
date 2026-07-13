class BaseScene:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        """이벤트 처리 """
        pass

    def update(self, dt):
        """상태 갱신"""
        pass

    def draw(self, screen):
        """화면 구성"""
        pass