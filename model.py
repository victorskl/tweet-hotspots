class Coord:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat


class Grid:
    def __init__(self, id, xmin, xmax, ymin, ymax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
