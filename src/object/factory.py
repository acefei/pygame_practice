#from bullet import *
from player import *
from enemy  import *
from utils.image_spliter import *


class GameObjectFactory(object):
    def __init__(self, settings):
        self.settings = settings
        self.init_bitmap()

    def init_bitmap(self):
        self.image = pygame.image.load(self.settings.SHOOT_IMAGE)
        self.image_pack = get_image_info(self.settings.SHOOT_IMAGE_PACK)

    def create_player(self, init_pos=(50,650)):
        return Player(self.image, self.image_pack, init_pos, self.settings)

    def create_enemy(self, init_pos=(120, 0)):
        return Enemy(self.image, self.image_pack, init_pos, self.settings)
