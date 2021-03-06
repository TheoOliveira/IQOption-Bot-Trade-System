# -*- coding: utf-8 -*-
"""Module for IQ Option TimeSync websocket object."""

import time
import datetime

from src.api.iqoption.ws.objects.base import Base


class TimeSync(Base):
    """Class for IQ Option TimeSync websocket object."""

    def __init__(self):
        super(TimeSync, self).__init__()
        self.__name = "timeSync"
        self.__server_timestamp = None
        self.__expiration_time = 1

    @property
    def server_timestamp(self):
        """Property to get server timestamp.

        :returns: The server timestamp.
        """
        return self.__server_timestamp / 1000

    @server_timestamp.setter
    def server_timestamp(self, timestamp):
        """Method to set server timestamp."""
        self.__server_timestamp = timestamp

    @property
    def server_datetime(self):
        """Property to get server datetime.

        :returns: The server datetime.
        """
        return datetime.datetime.fromtimestamp(self.server_timestamp)

    @property
    def expiration_minutes(self):
        """Property to get expiration time.

        :returns: The expiration time.
        """
        return self.__expiration_time

    @expiration_minutes.setter
    def expiration_minutes(self, minutes):
        """Method to set expiration time

        :param int minutes: The expiration time in minutes.
        """
        self.__expiration_time = minutes

    @property
    def expiration_datetime(self):
        """Property to get expiration datetime.

        :returns: The expiration datetime.
        """
        return self.server_datetime.replace(second=0, microsecond=0) + datetime.timedelta(minutes=self.expiration_minutes)

    @property
    def expiration_timestamp(self):
        """Property to get expiration timestamp.

        :returns: The expiration timestamp.
        """
        return time.mktime(self.expiration_datetime.timetuple())
