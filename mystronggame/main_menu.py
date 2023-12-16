import pygame
import sys
from button import ImageButton

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 960, 600
MAX_FPS = 60;

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DARK SOULS")
main_background = pygame.image.load("msg1019993666-77078.jpg")
clock = pygame.time.Clock()

# Загрузка и установка курсора
cursor = pygame.image.load("cursor_down_1.gif")
pygame.mouse.set_visible(False)  # Скрываем стандартынй курсор


def main_menu():
    '''Функция mainmenu() отвечает за создание и отображение интерфейса главного меню игры.
    Она инициализирует и обрабатывает кнопки запуска, настройки и выхода, а также их соответствующие функции
    Функция запускает цикл while для постоянного обновления и отображения главного меню, включая эффекты
    наведения кнопки и позиционирования курсора мыши

    :param : -
    :type : -
    :returns: None
    :rtype: None
    :raises None
    '''
    # Создание кнопок
    start_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "", "photo1701111581.jpeg",
                               "msg1199347004-77062.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    settings_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "", "msg1019993666-76746.jpg",
                                  "msg1019993666-76983.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    exit_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "", "msg1019993666-76983.jpg",
                              "msg1019993666-76984.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, -70 * (WIDTH / 960)))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("DARK SOULS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Старт' была нажата!")
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Кнопка 'Настройка' была нажата!")
                fade()
                settings_menu()
                for btn in [start_button, settings_button, exit_button]:
                    btn.set_pos(WIDTH / 2 - (252 / 2))

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def settings_menu():
    '''Функция создает меню настроек с кнопками аудио, видео и «Назад»
    Она включает в себя цикл while, который отображает фон и кнопки, а
    также обработку событий для нажатия кнопок или использования сочетаний клавиш.
    Пользователь может перемещаться по меню и изменять настройки.
    При нажатии кнопки аудио или видео отображаются соответствующие меню настроек, а
    кнопка «Назад» возвращает пользователя в предыдущее меню.
    Функция также обрабатывает наведение мыши и отображение курсора.

    :param : None
    :type : None
    :returns: None
    :rtype: None
    :raises None

    '''

    # Создание кнопок
    audio_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "", "msg1019993666-77075.jpg",
                               "msg1019993666-77076.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    video_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "", "msg1019993666-77080.jpg",
                               "msg1019993666-77076.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "", "msg1019993666-77079.jpg",
                              "msg1019993666-77076.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == video_button:
                print("Кнопка 'Настройки Видео' была нажата!")
                fade()
                video_settings_menu()
                for btn in [audio_button, video_button, back_button]:
                    btn.set_pos(WIDTH / 2 - (252 / 2))

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def video_settings_menu():
    '''Функция создает меню настроек видео с тремя кнопками режима видео и кнопкой «Назад»
    Онa включает в себя цикл while, который отображает фон и кнопки, а также обработку событий для нажатия кнопок
    или использования сочетаний клавиш.Пользователь может выбирать различные режимы видео с помощью кнопок,
    а кнопка «Назад» возвращает пользователя в предыдущее меню.Функция также обрабатывает наведение мыши, отображение курсора и обновление экрана.

    :param : None
    :type : None
    :returns: None
    :rtype: None
    :raises None

    '''
    video1_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "960x600", "msg962630647-78175.jpg",
                                "msg962630647-78178.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    video2_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "1280x800", "msg962630647-78175.jpg",
                                "msg962630647-78178.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    video3_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "1920x1080", "msg962630647-78175.jpg",
                                "msg962630647-78178.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "QUIT", "msg962630647-78175.jpg",
                              "msg962630647-78178.jpg", "dark-souls-you-died-sound-effect_hm5sYFG.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, -70))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("VIDEO SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            # d = {
            #     video1_button: (960, 600),
            #     video2_button: (1280, 800),
            #     video3_button: (1920, 1080)
            # }
            #
            # if event.type == pygame.USEREVENT and event.button in d.keys():
            #     change_vide_mode(d[event.button][0], d[event.button][1])
            #     fade()
            #     running = False

            d = {
                video1_button: (960, 600),
                video2_button: (1280, 800),
                video3_button: (1920, 1080)
            }

            for key in (d):
                if event.type == pygame.USEREVENT and event.button == key:
                    if key == video1_button:
                        change_vide_mode(960, 600)
                    elif key == video2_button:
                        change_vide_mode(1280, 800)
                    else:
                        change_vide_mode(1920, 1080, pygame.FULLSCREEN)

                    fade()
                    running = False

            # if event.type == pygame.USEREVENT and event.button == video1_button:
            #     change_vide_mode(960, 600)
            #     fade()
            #     running = False
            #
            # if event.type == pygame.USEREVENT and event.button == video2_button:
            #     change_vide_mode(1280, 800)
            #     fade()
            #     running = False
            #
            # if event.type == pygame.USEREVENT and event.button == video3_button:
            #     change_vide_mode(1920, 1080, pygame.FULLSCREEN)
            #     fade()
            #     running = False

            for btn in [video1_button, video2_button, video3_button, back_button]:
                btn.handle_event(event)
        flag = False
        if not (flag):
            for btn in [video1_button, video2_button, video3_button, back_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)
                flag = True

            # Отображение курсора в текущей позиции мыши
            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))

            pygame.display.flip()


def new_game():
    '''Функция new_game инициализирует новую игру в приложении
    Онa создает игровые кнопки и настраивает основной игровой цикл 
    для обработки игровых событий и рендеринга игрового экрана.
    В игровом цикле он постоянно проверяет игровые события, такие как   
    нажатие кнопок, наведение мыши и ввод с клавиатуры.Если обнаружено событие выхода или
     событие клавиши выхода, игра завершается.Онa также обрабатывает события
     мыши для кнопки «Назад», позволяя пользователю вернуться в главное меню.
     Когда функция выполняется, она отображает игровой экран и обновляет изображение.

    :param : None
    :type : None
    :returns: None
    :rtype: None
    :raises None

    '''
    # Создание кнопок
    back_button = ImageButton(WIDTH / 2 - (252 / 2), HEIGHT / 2 + 50, 252, 74, "", "msg1019993666-76983.jpg",
                              "msg1019993666-76984.jpg", "i-am-malenia-blade-of-miquella.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -80))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("A real warrior doesn't need a sword", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Возврат в меню
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover((pygame.mouse.get_pos()))
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


# затемнение
def fade():
    '''Функция Fade выполняет анимацию затухания текущего экрана.
    Уровень прозрачности анимации обновляется до тех пор, пока она не станет полностью затемненной.
    Анимация применяется к главному экрану с помощью библиотеки pygame.Функция работает
    в непрерывном цикле до тех пор, пока не будет достигнуто состояние.
    FRAMEHEIGHT и FRAMEWIDTH используются для создания поверхности, необходимой для анимации,
    а FPS (кадров в секунду) ограничивается для обеспечения плавности.

    :param : None
    :type : None
    :returns: None
    :rtype: None
    :raises None

    '''
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)  # Ограничение FPS


def change_vide_mode(w, h, fullscreen=0):
    '''Изменяет режим видео и устанавливает глобальные переменные screen и main_background

    :param w:Ширина видеорежима
    :param h:Высота видеорежима
    :param fullscreen:Указывает, должен ли видеорежим быть полноэкранным.
    :type w:int
    :type h:int
    :type fullscreen:int
    :returns: None
    :rtype: None
    :raises None

    '''


    global WIDTH, HEIGHT, screen, main_background

    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen)
    main_background = pygame.image.load(f'dark_souls_3_wallpaper600928.jpg')


if __name__ == "__main__":
    main_menu()
