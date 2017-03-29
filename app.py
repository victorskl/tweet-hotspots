import json
import logging

import core
from model import Coord

result = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0,
          'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'D3': 0, 'D4': 0, 'D5': 0}


def process(tweet_file):
    logging.info('Reading tweet JSON file:  %s', tweet_file)
    idx = 0
    skip = 0
    with open(tweet_file, encoding='utf8') as f:
        for line in f:

            # TODO ********** DEV STAB REMEMBER TO TAKE IT OUT!!! **********
            if idx > 668633: # 798202
                break

            try:
                tweet = json.loads(line)
                p = tweet['json']['coordinates']['coordinates']
                do_worker(Coord(p[0], p[1]), idx)
            except ValueError:
                try:
                    slice_line = line[:-2]
                    tweet = json.loads(slice_line)
                    p = tweet['json']['coordinates']['coordinates']
                    do_worker(Coord(p[0], p[1]), idx)
                except ValueError:
                    logging.info('Line is not a JSON String. Skip Index [%d]', idx)
                    logging.debug(line)
                    skip += 1
                    pass
            idx += 1

    logging.info('SUMMARY: total %d lines processed and skip %d lines.', idx + 1, skip)
    print(result)


def do_worker(coord, idx):
    if core.is_inside_super_grid(coord):
        print('Inside super grid: ', idx)
        gid = core.find_grid(coord)
        if gid is not None:
            result[gid] += 1


def main():
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('Tweet Hotspots Application Started!')

    core.init_grid('data/melbGrid.json')

    process('data/bigTwitter.json')


if __name__ == '__main__':
    main()
