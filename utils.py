import logging

SORT_BY_BOX = 'Order (rank) the Grid boxes based on the total number of tweets made in each box'
SORT_BY_ROW = 'Order (rank) the rows based on the total number of tweets in each row'
SORT_BY_COL = 'Order (rank) the columns based on the total number of tweets in each column'


def print_sort_box_header():
    print_header(SORT_BY_BOX)


def print_sort_row_header():
    print_header(SORT_BY_ROW)


def print_sort_col_header():
    print_header(SORT_BY_COL)


def print_header(label):
    print(label)
    print("-" * 78)
    logging.info(label)
    # logging.info("-" * 78)
