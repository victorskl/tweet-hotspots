import logging
import json

from model import Grid

grids = {}


def init_grid(melbgrid_json_file):
    with open(melbgrid_json_file) as f:
        melbgrid = json.load(f)
        features = melbgrid['features']
        for feature in features:
            properties = feature['properties']
            id = properties['id']
            xmin = properties['xmin']
            xmax = properties['xmax']
            ymin = properties['ymin']
            ymax = properties['ymax']
            grids[id] = Grid(id, xmin, xmax, ymin, ymax)
        logging.info('Successfully initialized melbGrid:  %s', melbgrid_json_file)


def is_inside_super_grid(coord):
    if coord.lon < 0:
        return False

    if coord.lat > 0:
        return False

    a1 = grids['A1']
    d5 = grids['D5']

    abs_d5_ymin = abs(d5.ymin)
    abs_a1_ymax = abs(a1.ymax)
    abs_lat = abs(coord.lat)

    if a1.xmin <= coord.lon <= d5.xmax:
        if abs_a1_ymax <= abs_lat <= abs_d5_ymin:
            return True
    else:
        return False
