from pprint import pprint

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
