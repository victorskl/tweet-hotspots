import json
import logging
from collections import Counter
from datetime import datetime
from timeit import default_timer as timer

from mpi4py import MPI

import core
import sequential as sq
import utils
from model import Coord

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
status = MPI.Status()

READY = 1
START = 2
DONE = 3
EXIT = 4
ABORT = 5

result = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0,
          'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'D3': 0, 'D4': 0, 'D5': 0}


def do_master(tweet_file):
    logging.info('Reading tweet JSON file:  %s', tweet_file)
    idx = 0
    skip = 0
    with open(tweet_file, encoding='utf8') as f:
        for line in f:
            comm.recv(source=MPI.ANY_SOURCE, tag=READY, status=status)
            source = status.Get_source()
            try:
                tweet = json.loads(line)
                p = tweet['json']['coordinates']['coordinates']
                # print('Send ', idx, ' to rank ', source)
                comm.send(p, dest=source, tag=START)
            except ValueError:
                try:
                    slice_line = line[:-2]
                    tweet = json.loads(slice_line)
                    p = tweet['json']['coordinates']['coordinates']
                    # print('Send ', idx, ' to rank ', source)
                    comm.send(p, dest=source, tag=START)
                except ValueError:
                    logging.info('Line is not a JSON String. Skip Index [%d]', idx)
                    # print(line)
                    comm.send(None, dest=source, tag=ABORT)
                    skip += 1
                    continue
            idx += 1

    logging.info('SUMMARY: total %d lines processed and skip %d lines.', idx + 1, skip)


def do_slave():
    while True:
        comm.send(None, dest=0, tag=READY)
        p = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
        tag = status.Get_tag()

        if tag == START:
            coord = Coord(p[0], p[1])
            if core.is_inside_super_grid(coord):
                gid = core.find_grid(coord)
                if gid is not None:
                    result[gid] += 1
        elif tag == EXIT:
            comm.send(result, dest=0, tag=DONE)
            break
        elif tag == ABORT:
            continue


def do_parallel(twitter_json):
    if rank == 0:
        do_master(twitter_json)
    else:
        do_slave()

    if rank == 0:
        summing = {'A1': 1, 'A2': 1, 'A3': 1, 'A4': 1,
                   'B1': 1, 'B2': 1, 'B3': 1, 'B4': 1,
                   'C1': 1, 'C2': 1, 'C3': 1, 'C4': 1, 'C5': 1,
                   'D3': 1, 'D4': 1, 'D5': 1}

        for i in range(size - 1):
            node = i + 1
            comm.send(None, dest=node, tag=EXIT)
            local_result = comm.recv(source=node, tag=DONE, status=status)
            # print(local_result)
            summing = Counter(summing) + Counter(local_result)

        d = dict(summing)

        # Printing the result

        utils.print_sort_box_header()
        for k in sorted(d, key=d.get, reverse=True):
            out = '%s: %d tweets' % (k, d[k] - 1)
            print(out)
            logging.info(out)

        row = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        col = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
        for key, value in d.items():
            if key.startswith('A'):
                row['A'] += value - 1
            if key.startswith('B'):
                row['B'] += value - 1
            if key.startswith('C'):
                row['C'] += value - 1
            if key.startswith('D'):
                row['D'] += value - 1
            if key.endswith('1'):
                col['1'] += value - 1
            if key.endswith('2'):
                col['2'] += value - 1
            if key.endswith('3'):
                col['3'] += value - 1
            if key.endswith('4'):
                col['4'] += value - 1
            if key.endswith('5'):
                col['5'] += value - 1

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


def main():
    global t_start
    if rank == 0:
        t_start = timer()
        logging.basicConfig(
            filename='app_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.log',
            filemode='w',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.info('Tweet Hotspots Application Started!')
        logging.info('Number of processors:  %d', size)
        if size < 2:
            logging.info('Redirecting to sequential geo-processing...')
        else:
            logging.info('Initiating parallel geo-processing...')

    grid_json = 'data/melbGrid.json'
    twitter_json = 'data/bigTwitter.json'

    core.init_grid(grid_json)

    if rank == 0 and size < 2:
        sq.process(twitter_json)
    else:
        do_parallel(twitter_json)

    if rank == 0:
        t_end = timer()
        time_taken = 'It takes %.18f seconds.' % (t_end - t_start)
        print('\n')
        print(time_taken)
        logging.info(time_taken)


if __name__ == '__main__':
    main()
