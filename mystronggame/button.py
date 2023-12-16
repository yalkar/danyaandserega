import pygame


class ImageButton:
    '''Класс для создания интерактивной кнопки изображения с дополнительным эффектом наведения и звуком.
       :param x: координата x кнопки
       :param y: координата y кнопки
       :param width: ширина кднопки
       :param height: высота кнопки
       :param text: текст, отображаемый на кнопке
       :param image_path: путь к файлу изображения кнопки
       :param hover_image_path:путь к файлу альтернативного изображения кнопки для эффекта наведения
       :param sound_path:путь к файлу звукового эффекта, который будет воспроизводиться при нажатии кнопки
       :type x:int
       :type y:int
       :type width:int
       :type height:int
       :type text:str
       :type image_path:str
       :type hover_image_path:str, optional
       :type sound_path:str, optional
       :returns: None
       :rtype: None
       :raises None
    '''

    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def set_pos(self, x, y=None):
        '''Метод set_pos устанавливает позицию обьекта по горизонтальной x и
        вертикальной y координатам
        :param x: Горизонтальная координата позиции обьекта
        :param y: Вертикальная координата позиция
        :type x:int
        :type y: int
        :returns: None
        :rtype: None
        :raises None
        '''
        self.x = x
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        '''Отображает элемент интерфейса на экране


        :param screen: объект отображения pygame, на котором будет отображаться элемент
        :type screen: class
        :returns: None
        :rtype: None
        :raises None
        '''
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        '''Проверяет, наведен ли курсор мыши на элемент

        :param mouse_pos: кортеж с координатами положения курсора мыши
        :type mouse_pos: tuple
        :returns: None
        :rtype: None
        :raises None
        '''
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        '''Обрабатывает события для элемента интерфейса
        :param event: объект события pygame
        :type event: class
        :returns: None
        :rtype: None
        :raises None
        :Side Effects:Воспроизводит звуковой эффект, если указанное событие является нажатием левой кнопки мыши над
         элементом интерфейса с установленным флагом is_hovered в True. Далее поднимает событие pygame.USEREVENT с
         передачей элемента интерфейса в качестве атрибута кнопки.
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
