import unittest
import core
from model import Coord


def _init():
    core.init_grid('data/melbGrid.json')


class AppTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_super_grid_bound(self):

        _init()

        coord_ok = Coord(144.8354, -37.826534)
        coord_both_out = Coord(138.595998, -34.9226534)
        coord_lon_out = Coord(148.8354, -37.826534)
        coord_lat_out = Coord(145.1, -34.9226534)
        coord_x = Coord(-145.45, -34.9226534)
        coord_xx = Coord(145.45, 34.9226534)

        self.assertTrue(core.is_inside_super_grid(coord_ok))
        self.assertFalse(core.is_inside_super_grid(coord_both_out))
        self.assertFalse(core.is_inside_super_grid(coord_lon_out))
        self.assertFalse(core.is_inside_super_grid(coord_lat_out))
        self.assertFalse(core.is_inside_super_grid(coord_x))
        self.assertFalse(core.is_inside_super_grid(coord_xx))


if __name__ == '__main__':
    unittest.main()
