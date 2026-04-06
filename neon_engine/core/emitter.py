from .particle import Particle

class Emitter:
    def __init__(self):
        self.particles = []

    def emit(self, position):
        """Добавление новых объектов в систему."""
        for _ in range(5):
            self.particles.append(Particle(position))

    def update(self):
        """Массовое обновление и очистка памяти."""
        for p in self.particles:
            p.update()
        
        # 7. Фильтрация: Удаление мертвых объектов
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)
