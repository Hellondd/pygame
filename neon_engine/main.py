import pygame
import sys
from core.emitter import Emitter

def main():
    # 8. pygame.init: Инициализация всех модулей
    pygame.init()
    
    # 9. pygame.display: Настройка окна
    screen = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption("Neon Particle Engine v1.0")
    
    # 10. pygame.time.Clock: Контроль FPS
    clock = pygame.time.Clock()
    emitter = Emitter()
    
    running = True
    while running:
        # 11. pygame.event: Обработка очереди событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 12. pygame.mouse: Взаимодействие с вводом
            if event.type == pygame.MOUSEBUTTONDOWN:
                emitter.emit(event.pos)

        if pygame.mouse.get_pressed()[0]:
            emitter.emit(pygame.mouse.get_pos())

        # Очистка экрана (черный фон)
        screen.fill((0, 0, 0))

        # Обновление и отрисовка
        emitter.update()
        emitter.draw(screen)

        # 13. pygame.display.flip: Обновление кадра
        pygame.display.flip()
        
        # Ограничение до 60 кадров в секунду
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
