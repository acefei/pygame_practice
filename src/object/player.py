import pygame
from bullet import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image, image_pack, init_pos, settings):
        pygame.sprite.Sprite.__init__(self)
        self._image = image
        self._image_pack = image_pack
        self._set_player_rect(image_pack)
        self._set_player_image(image)

        self.rect = self.player_rect[0]
        self.rect.topleft = init_pos

        self.speed = settings.PLAYER_SPEED
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False
        self.settings = settings


    def _set_player_rect(self, image_pack):
        self.player_rect = []
        for k in sorted(image_pack.keys()):
            if 'hero' not in k:
                continue
            (left, top) = map(int, image_pack[k]['xy'].split(','))
            (width, height) = map(int, image_pack[k]['size'].split(','))
            self.player_rect.append(pygame.Rect(left, top, width, height))

    def _set_player_image(self, image):
        self.player_image = []
        for i, _ in enumerate(self.player_rect):
            self.player_image.append(image.subsurface(self.player_rect[i]).convert_alpha())

    def draw(self, view, img_index):
        view.screen.blit(self.player_image[img_index], self.rect)

    def shoot(self):
        bullet = Bullet(self._image, self._image_pack, self.rect.midtop, self.settings)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= self.settings.SCREEN_HEIGHT - self.rect.height:
            self.rect.top = self.settings.SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= self.settings.SCREEN_WIDTH - self.rect.width:
            self.rect.left = self.settings.SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
