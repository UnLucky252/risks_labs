import pygame
import os
import sys

# Установка dummy драйвера для работы без дисплея
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def main():
    pygame.init()
    
    # Создаем поверхность в памяти (без окна)
    screen = pygame.Surface((800, 600))
    
    # Заливаем фон
    screen.fill((255, 255, 255))
    
    # Создаем текст
    try:
        font = pygame.font.Font(None, 75)
    except:
        font = pygame.font.SysFont(None, 75)
    
    text = font.render("Hello AppSec World!", True, (0, 255, 0))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    
    # Сохраняем результат в файл
    pygame.image.save(screen, "output.png")
    print("✅ Изображение сохранено как 'output.png'")
    print("🎮 Pygame инициализирован успешно")
    print("👋 Hello AppSec World!")
    
    pygame.quit()

if __name__ == "main":
    main()
