#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Ryan Mackenzie White <ryan.white4@canada.ca>
#
# Distributed under terms of the Copyright © Her Majesty the Queen in Right of Canada, as represented by the Minister of Statistics Canada, 2019. license.

"""
Dummy Tool
"""
from pprint import pformat
import logging
import sys

from artemis_base.core.tool import ToolBase
from artemis_base.utils.decorators import timethis


class DummyTool(ToolBase):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.__logger.debug(pformat(kwargs))
        self.__logger.debug(pformat(self.__dict__))
        self.__logger.debug(pformat(self.__class__.__dict__))
        self.__logger.info("%s: Initialized DummyTool" % self.name)

    def initialize(self):
        self.__logger.info(self.__logger)
        self.__logger.info(self._DummyTool__logger)
        self.__logger.info("%s: property %s" % (self.name, self.properties.myproperty))

    def book(self):
        pass

    @timethis
    def execute(self, payload):
        if logging.getLogger().isEnabledFor(
            logging.DEBUG
        ) or self.__logger.isEnabledFor(logging.DEBUG):

            # Prevent excessive formating calls when not required
            # Note that we can indepdently change the logging level
            # for algo loggers and root logger
            # Use string interpolation to prevent excessive format calls
            self.__logger.debug("%s: execute " % self.name)
            # Check logging level if formatting requiered
            self.__logger.debug(
                "{}: execute: payload {}".format(self.name, sys.getsizeof(payload))
            )

        self.__logger.debug("Trying to debug")

    def finalize(self):
        pass
