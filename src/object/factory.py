from bullet import *
from player import *
from enemy  import *
from utils.image_spliter import *


class GameObjectFactory(object):
    def __init__(self, settings):
        self.settings = settings
        self.init_bitmap()
        self.set_player_rect()

    def init_bitmap(self):
        self.image = pygame.image.load(self.settings.SHOOT_IMAGE)
        self.image_pack = get_image_info(self.settings.SHOOT_IMAGE_PACK)

    def set_player_rect(self):
        self.player_rect = []
        for k in self.image_pack.keys():
            if 'hero' not in k:
                continue
            (left, top) = map(int, self.image_pack[k]['xy'].split(','))
            (width, height) = map(int, self.image_pack[k]['size'].split(','))
            self.player_rect.append(pygame.Rect(left, top, width, height))

    def create_player(self):
        player_init_pos = [50, 650]
        return Player(self.image, self.player_rect, player_init_pos, self.settings)

