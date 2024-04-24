class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initial default Television settings
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Power status of the Television
        """
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False

    def mute(self) -> None:
        """
        Mute status of television
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increasing channel
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreasing channel
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Raising television volume
        """
        if self.__status and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreasing television volume
        """
        if self.__status and self.__volume > self.MIN_VOLUME:
            self.__volume = 1
        if self.__status and self.__volume < self.MIN_VOLUME:
            self.__volume = 0

    def __str__(self) -> str:
        """
        :return: Returning television objects
        """
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
