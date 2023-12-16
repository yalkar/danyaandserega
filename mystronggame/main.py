import pygame
import sys
from button import ImageButton

# Инициализация pygame
pygame.init()

# Парметры экрана
WIDTH, HEIGHT = 600, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button test")

# Создание кнопки
green_button = ImageButton(WIDTH/2-(252/2), 100, 252, 74, "", "photo1701111581.jpeg", "msg1019993666-76581.jpg", "movie_1.mp3")

green_button2 = ImageButton(WIDTH/2-(252/2), 300, 252, 74, "", "msg1019993666-76746.jpg", "msg1019993666-76983.jpg", "movie_1.mp3")

red_button = ImageButton(WIDTH/2-(252/2), 200, 252, 74, "", "msg1019993666-76983.jpg", "msg1019993666-76984.jpg", "movie_1.mp3")

icon_button = ImageButton(WIDTH/2-(252/2), 400, 85, 85, "", "1695918239_gas-kvas-com-p-kartinki-mech-30.png", "msg1019993666-76987.jpg", "movie_1.mp3")

icon_button2 = ImageButton(320, 400, 85, 85, "", "900px-SR-icon-spell-Illusion_Dark.png", "msg1019993666-76988.jpg", "movie_1.mp3")

def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("DARK SOULS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(300,50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == green_button:
                print("Кнопка 'Первая' была нажата!")

            if event.type == pygame.USEREVENT and event.button == green_button2:
                print("Кнопка 'Третья' была нажата!")
                # Здесь вы можете вызвать функцию или событие, которое начнет игру

            green_button.handle_event(event)
            green_button2.handle_event(event)

        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        green_button2.check_hover(pygame.mouse.get_pos())
        green_button2.draw(screen)
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        icon_button.check_hover(pygame.mouse.get_pos())
        icon_button.draw(screen)
        icon_button2.check_hover(pygame.mouse.get_pos())
        icon_button2.draw(screen)
        pygame.display.flip()

main_menu()







