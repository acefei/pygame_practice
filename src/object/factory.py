#from bullet import *
from player import *
from enemy  import *
from utils.image_spliter import *


class GameObjectFactory(object):
    def __init__(self, settings):
        self.settings = settings
        self.init_bitmap()
        self.set_bullet1_rect()
        self.set_enemy1_rect()

    def init_bitmap(self):
        self.image = pygame.image.load(self.settings.SHOOT_IMAGE)
        self.image_pack = get_image_info(self.settings.SHOOT_IMAGE_PACK)

    def create_player(self):
        player_init_pos = [50, 650]
        return Player(self.image, self.image_pack, player_init_pos, self.settings)

    def set_bullet1_rect(self):
        k = 'bullet1'
        (left, top) = map(int, self.image_pack[k]['xy'].split(','))
        (width, height) = map(int, self.image_pack[k]['size'].split(','))
        print "-----------", k, left, top, width, height
        self.bullet1_rect = pygame.Rect(left, top, width, height)

    @property
    def bullet1_img(self):
        return self.image.subsurface(self.bullet1_rect)

    def create_enemies(self, enemy_frequency):
        if enemy_frequency % 50 == 0:
            enemy1_init_pos = [random.randint(0, self.settings.SCREEN_WIDTH - enemy1_rect.width), 0]
            enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_init_pos)
            enemies1.add(enemy1)

    def set_enemy1_rect(self):
        k = 'enemy1'
        (left, top) = map(int, self.image_pack[k]['xy'].split(','))
        (width, height) = map(int, self.image_pack[k]['size'].split(','))
        self.enemy1_rect = pygame.Rect(left, top, width, height)

    @property
    def enemy1_img(self):
        return self.image.subsurface(self.enemy1_rect)
