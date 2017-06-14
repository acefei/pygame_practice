from pprint import pprint
import pygame


def get_image_info(pack_file):
    with open(pack_file) as f:
        thing = f.readlines()

    res = {}
    for l in thing:
        l = l.strip()
        if not l.split():
            continue

        d = l.split(':')
        if len(d) != 2:
            role = l
            res[role] = {}
            continue

        k, v = d[0], d[1]
        res[role][k] = v
    #pprint(res)
    return res

def get_sub_image(name, image, image_pack):
    '''
       options:
           name: game object name
           image: pygame image instance
           image_pack: A dict with image rectangle info

       return:
           image rectangle, image subsurface instance
    '''
    if name in image_pack:
        (left, top) = map(int, image_pack[name]['xy'].split(','))
        (width, height) = map(int, image_pack[name]['size'].split(','))
        rect = pygame.Rect(left, top, width, height)
        return rect, image.subsurface(rect)
    else:
        return None, None

