import json
import logging

from model import Grid

grids = {}


def init_grid(melbgrid_json_file):
    with open(melbgrid_json_file, encoding='utf8') as f:
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


def is_z1_or_z2(coord):
    b1 = grids['B1']
    if abs(coord.lat) < abs(b1.ymin):
        return 'z1'
    else:
        return 'z2'


def is_zab(coord):
    a4 = grids['A4']
    if coord.lon > a4.xmax:
        return False
    else:
        return True


def is_za_or_zb(coord):
    a1 = grids['A1']
    if abs(coord.lat) < abs(a1.ymin):
        return 'za'
    else:
        return 'zb'


def is_za12_or_za34(coord):
    a3 = grids['A3']
    if coord.lon < a3.xmin:
        return 'za12'
    else:
        return 'za34'


def is_a1_or_a2(coord):
    a2 = grids['A2']
    if coord.lon < a2.xmin:
        return 'a1'
    else:
        return 'a2'


def is_a3_or_a4(coord):
    a4 = grids['A4']
    if coord.lon < a4.xmin:
        return 'a3'
    else:
        return 'a4'


def is_zb12_or_zb34(coord):
    b3 = grids['B3']
    if coord.lon < b3.xmin:
        return 'zb12'
    else:
        return 'zb34'


def is_b1_or_b2(coord):
    b2 = grids['B2']
    if coord.lon < b2.xmin:
        return 'b1'
    else:
        return 'b2'


def is_b3_or_b4(coord):
    b4 = grids['B4']
    if coord.lon < b4.xmin:
        return 'b3'
    else:
        return 'b4'


def is_zc_or_zd(coord):
    c1 = grids['C1']
    if abs(coord.lat) < abs(c1.ymin):
        return 'zc'
    else:
        return 'zd'


def is_zc12_or_zc345(coord):
    c3 = grids['C3']
    if coord.lon < c3.xmin:
        return 'zc12'
    else:
        return 'zc345'


def is_c1_or_c2(coord):
    c2 = grids['C2']
    if coord.lon < c2.xmin:
        return 'c1'
    else:
        return 'c2'


def is_c3_or_c45(coord):
    c4 = grids['C4']
    if coord.lon < c4.xmin:
        return 'c3'
    else:
        return 'c45'


def is_c4_or_c5(coord):
    c5 = grids['C5']
    if coord.lon < c5.xmin:
        return 'c4'
    else:
        return 'c5'


def is_zd345(coord):
    d3 = grids['D3']
    if coord.lon < d3.xmin:
        return False
    else:
        return True


def is_d3_or_d45(coord):
    d4 = grids['D4']
    if coord.lon < d4.xmin:
        return 'd3'
    else:
        return 'd45'


def is_d4_or_d5(coord):
    d5 = grids['D5']
    if coord.lon < d5.xmin:
        return 'd4'
    else:
        return 'd5'


def find_grid(coord):
    # print('[%.8f, %.8f]' % (coord.lon, coord.lat))
    if is_z1_or_z2(coord) == 'z1':
        # print('inside z1')
        if is_zab(coord):
            # print('-inside zab')
            if is_za_or_zb(coord) == 'za':
                # print('--inside za')
                if is_za12_or_za34(coord) == 'za12':
                    # print('---inside za12')
                    if is_a1_or_a2(coord) == 'a1':
                        # print('----inside a1')
                        return 'A1'
                    else:
                        # print('----inside a2')
                        return 'A2'
                else:
                    # print('---inside za34')
                    if is_a3_or_a4(coord) == 'a3':
                        # print('----inside a3')
                        return 'A3'
                    else:
                        # print('----inside a4')
                        return 'A4'
            else:
                # print('--inside zb')
                if is_zb12_or_zb34(coord) == 'zb12':
                    # print('---inside zb12')
                    if is_b1_or_b2(coord) == 'b1':
                        # print('----inside b1')
                        return 'B1'
                    else:
                        # print('----inside b2')
                        return 'B2'
                else:
                    # print('---inside zb34')
                    if is_b3_or_b4(coord) == 'b3':
                        # print('----inside b3')
                        return 'B3'
                    else:
                        # print('----inside b4')
                        return 'B4'
        else:
            # print('z1 void zone')
            pass

    elif is_z1_or_z2(coord) == 'z2':
        # print('inside z2')
        if is_zc_or_zd(coord) == 'zc':
            # print('-inside zc')
            if is_zc12_or_zc345(coord) == 'zc12':
                # print('--inside zc12')
                if is_c1_or_c2(coord) == 'c1':
                    # print('---inside c1')
                    return 'C1'
                else:
                    # print('---inside c2')
                    return 'C2'
            else:
                # print('--inside zc345')
                if is_c3_or_c45(coord) == 'c3':
                    # print('---inside c3')
                    return 'C3'
                else:
                    # print('---inside c45')
                    if is_c4_or_c5(coord) == 'c4':
                        # print('----inside c4')
                        return 'C4'
                    else:
                        # print('----inside c5')
                        return 'C5'
        else:
            # print('-inside zd')
            if is_zd345(coord):
                # print('--inside zd345')
                if is_d3_or_d45(coord) == 'd3':
                    # print('---inside d3')
                    return 'D3'
                else:
                    # print('---inside d45')
                    if is_d4_or_d5(coord) == 'd4':
                        # print('----inside d4')
                        return 'D4'
                    else:
                        # print('----inside d5')
                        return 'D5'
            else:
                # print('zd void zone')
                pass

    else:
        # print('fallout!')
        pass
