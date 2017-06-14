import pygame
from utils.image_spliter import get_sub_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, image_pack, init_pos, settings):
        pygame.sprite.Sprite.__init__(self)
        self.rect, self.image = get_sub_image('bullet1', image, image_pack)
        self.rect.midbottom = init_pos
        self.speed = settings.BULLET_SPEED

    def move(self):
        self.rect.top -= self.speed
