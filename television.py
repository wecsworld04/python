class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initial default Television settings
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """
        Power status of the Television
        """
        self.__status = not self.__status

    def mute(self):
        """
        Mute status of television
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increasing channel
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        decreasing channel
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        raising television volume
        """
        if self.__status:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            elif self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        """
        decreasing television volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        :return: Returning television objects
        """
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
