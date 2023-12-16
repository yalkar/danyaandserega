import pygame
import unittest
from button import ImageButton


class TestImageButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.image_button = ImageButton(100, 100, 150, 50, "Click me", "msg1019993666-77080.jpg")

    def tearDown(self):
        pygame.quit()

    def test_init_without_hover_image_or_sound(self):
        self.assertEqual(self.image_button.x, 100)
        self.assertEqual(self.image_button.y, 100)
        self.assertEqual(self.image_button.width, 150)
        self.assertEqual(self.image_button.height, 50)
        self.assertEqual(self.image_button.text, "Click me")
        self.assertEqual(self.image_button.image.get_rect().size, (150, 50))
        self.assertEqual(self.image_button.hover_image.get_rect().size, (150, 50))
        self.assertEqual(self.image_button.rect.topleft, (100, 100))
        self.assertIsNone(self.image_button.sound)
        self.assertFalse(self.image_button.is_hovered)

    def test_init_with_hover_image_and_sound(self):
        image_button_with_hover = ImageButton(200, 200, 150, 50, "Hover me", "msg1019993666-77080.jpg",
                                              "msg1019993666-77075.jpg", "i-am-malenia-blade-of-miquella.mp3")
        self.assertEqual(image_button_with_hover.hover_image.get_rect().size, (150, 50))
        self.assertIsNotNone(image_button_with_hover.sound)


if __name__ == '__main__':
    unittest.main()
