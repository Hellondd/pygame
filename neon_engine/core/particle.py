import pygame
import random

class Particle:
    """Объект частицы с физикой движения."""
    def __init__(self, position):
        # 1. pygame.math.Vector2: Работа с 2D векторами
        self.pos = pygame.math.Vector2(position)
        self.vel = pygame.math.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        self.acc = pygame.math.Vector2(0, 0.1) # Гравитация
        
        # 2. pygame.Color: Управление цветом и прозрачностью
        self.color = pygame.Color(0)
        self.color.hsla = (random.randint(0, 360), 100, 50, 100)
        
        self.lifetime = 255.0
        self.decay = random.uniform(1.5, 3.0)
        self.radius = random.randint(4, 8)

    def update(self):
        """Обновление физического состояния."""
        self.vel += self.acc
        self.pos += self.vel
        self.lifetime -= self.decay
        if self.radius > 0.1:
            self.radius -= 0.05

    def draw(self, surface):
        """
        3. pygame.Surface: Создание временной поверхности для свечения.
        4. pygame.draw.circle: Отрисовка геометрии.
        """
        if self.lifetime <= 0:
            return

        # Создаем эффект свечения через отдельную поверхность
        size = int(self.radius * 2.5)
        glow_surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        
        # 5. Смешивание цветов: градиентное затухание
        alpha = max(0, int(self.lifetime))
        color_with_alpha = (*self.color[:3], alpha // 2)
        
        pygame.draw.circle(glow_surf, color_with_alpha, (size, size), size)
        
        # 6. BLEND_RGB_ADD: Аддитивное наложение для эффекта неона
        surface.blit(glow_surf, (int(self.pos.x - size), int(self.pos.y - size)), special_flags=pygame.BLEND_RGB_ADD)
        pygame.draw.circle(surface, (*self.color[:3], alpha), (int(self.pos.x), int(self.pos.y)), int(self.radius))
