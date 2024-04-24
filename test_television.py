import pytest
from television import Television


class Test:
    def test_init(self):
        assert str(Television()) == "Power = [False], Channel = [0], Volume = [0]"

    def test_power(self):
        tv = Television()
        tv.power()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.power()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"

    def test_mute(self):
        tv = Television()
        tv.power()
        tv.mute()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.mute()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.power()
        tv.mute()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"
        tv.power()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"

    def test_channel_up(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        assert str(tv) == "Power = [True], Channel = [1], Volume = [0]"
        tv.channel_up()
        assert str(tv) == "Power = [True], Channel = [2], Volume = [0]"
        tv.channel_up()
        assert str(tv) == "Power = [True], Channel = [3], Volume = [0]"
        tv.channel_up()
        assert str(
            tv) == "Power = [True], Channel = [0], Volume = [0]"

    def test_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [3], Volume = [0]"
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [2], Volume = [0]"
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [1], Volume = [0]"
        tv.channel_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"

    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"
        tv.volume_up()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"  # Max volume should not exceed 2

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.volume_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
        tv.volume_up()
        tv.volume_down()
        assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"

    if __name__ == "__main__":
        pytest.main()
