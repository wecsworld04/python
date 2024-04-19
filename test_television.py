import unittest

import pytest
from television import *

class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Television()._Television__status, False)
        self.assertEqual(Television()._Television__muted, False)
        self.assertEqual(Television()._Television__volume, 0)
        self.assertEqual(Television()._Television__channel, 0)

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertEqual(tv._Television__status, True)

    def test_mute(self):
        tv = Television()
        tv.mute()
        self.assertEqual(tv._Television__muted, False)

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        self.assertEqual(tv._Television__channel, 0)
        tv._Television__channel = 0
        tv.channel_up()
        self.assertEqual(tv._Television__channel, 0)

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        self.assertEqual(tv._Television__channel, 0)
        tv._Television__channel = 3
        tv.channel_down()
        self.assertEqual(tv._Television__channel, 3)

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 0)
        tv._Television__volume = 2
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 2)

    def test_volume_down(self):
        tv = Television()
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 0)
        tv._Television__volume = 0
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 0)

if __name__ == '__main__':
    unittest.main()