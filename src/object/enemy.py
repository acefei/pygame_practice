import pygame
from utils.image_spliter import get_sub_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, image_pack, init_pos, settings):
       pygame.sprite.Sprite.__init__(self)
       self._image = image
       self._image_pack = image_pack
       self._set_enemy()
       self._set_enemy_down()

       self.rect = self.enemy_rect
       self.rect.topleft = init_pos

       self.down_imgs = enemy_down_imgs
       self.speed = settings.ENEMY_SPEED
       self.down_index = 0

    def _set_enemy(self):
        self.enemy_rect, self.enemy_image = get_sub_image('enemy1', self._image, self._image_pack)

    def _set_enemy_down(self):
        self.enemy_down_images = []
        for k in sorted(image_pack.keys()):
            if 'enemy1_down' not in k:
                continue
            _, enemy_down_image = get_sub_image(k, self._image, self._image_pack)
            self.enemy_down_images.append(enemy_down_image)

    def move(self):
        self.rect.top += self.speed
