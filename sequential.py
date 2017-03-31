import json
import logging

import core
import utils
from model import Coord

result = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0,
          'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'D3': 0, 'D4': 0, 'D5': 0}


def process(tweet_file):
    logging.info('Reading tweet JSON file:  %s', tweet_file)
    idx = 0
    skip = 0
    with open(tweet_file, encoding='utf8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                p = tweet['json']['coordinates']['coordinates']
                search_by_coord(Coord(p[0], p[1]))
            except ValueError:
                try:
                    slice_line = line[:-2]
                    tweet = json.loads(slice_line)
                    p = tweet['json']['coordinates']['coordinates']
                    search_by_coord(Coord(p[0], p[1]))
                except ValueError:
                    logging.info('Line is not a JSON String. Skip Index [%d]', idx)
                    logging.debug(line)
                    skip += 1
                    continue
            idx += 1

    logging.info('SUMMARY: total %d lines processed and skip %d lines.', idx + 1, skip)
    print_result()


def search_by_coord(coord):
    if core.is_inside_super_grid(coord):
        gid = core.find_grid(coord)
        if gid is not None:
            result[gid] += 1


def print_result():
    utils.print_sort_box_header()
    for k in sorted(result, key=result.get, reverse=True):
        out = '%s: %d tweets' % (k, result[k])
        print(out)
        logging.info(out)

    row = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    col = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
    for key, value in result.items():
        if key.startswith('A'):
            row['A'] += value
        if key.startswith('B'):
            row['B'] += value
        if key.startswith('C'):
            row['C'] += value
        if key.startswith('D'):
            row['D'] += value
        if key.endswith('1'):
            col['1'] += value
        if key.endswith('2'):
            col['2'] += value
        if key.endswith('3'):
            col['3'] += value
        if key.endswith('4'):
            col['4'] += value
        if key.endswith('5'):
            col['5'] += value

    utils.print_sort_row_header()
    for k in sorted(row, key=row.get, reverse=True):
        out = '%s-Row: %d tweets' % (k, row[k])
        print(out)
        logging.info(out)

    utils.print_sort_col_header()
    for k in sorted(col, key=col.get, reverse=True):
        out = 'Column %s: %d tweets' % (k, col[k])
        print(out)
        logging.info(out)
