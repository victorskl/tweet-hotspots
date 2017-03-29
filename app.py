import logging
import json
import core
from model import Coord

limit = 30000


def read(tweet_file):
    logging.info('Reading tweet JSON file:  %s', tweet_file)
    idx = 0
    skip = 0
    with open(tweet_file) as f:
        for line in f:

            # TODO to be removed once finalize
            if idx > limit:
                break

            try:
                tweet = json.loads(line)
                p = tweet['json']['coordinates']['coordinates']
                do_worker(Coord(p[0], p[1]))
            except ValueError:
                try:
                    slice_line = line[:-2]
                    tweet = json.loads(slice_line)
                    p = tweet['json']['coordinates']['coordinates']
                    do_worker(Coord(p[0], p[1]))
                except ValueError:
                    logging.info('Line is not a JSON String. Skip Index [%d]', idx)
                    logging.debug(line)
                    skip += 1
                    pass
            idx += 1

        logging.info('SUMMARY: total %d lines processed and skip %d lines.', idx + 1, skip)


def do_worker(coord):
    # print 'worker task'
    if core.is_inside_super_grid(coord):
        print 'inside super grid'


def main():
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('Tweet Hotspots Application Started!')

    core.init_grid('data/melbGrid.json')

    read('data/smallTwitter.json')


if __name__ == '__main__':
    main()
