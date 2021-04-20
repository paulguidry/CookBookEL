#!/usr/bin/env python
from math import ceil
import logging
from datetime import datetime
import traceback
import sys
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

try:
    import ConstantUtil as cu
except ModuleNotFoundError as mnfe:
    from CookBookEL import ConstantUtil as cu



def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]

    return exception_str


class LOG_FILE_INTERVAL_C(cu.Const):

    NOTSET: int = 0
    MINUTE: int = 1
    HOUR: int = 2
    DAY: int = 3
    WEEK: int = 4
    MONTH: int = 5
    YEAR: int = 6


    @classmethod
    def __week_of_month(cls, p_datetime: datetime):
        """ Returns the week of the month for the specified date.
        """
        first_day = p_datetime.replace(day=1)
        dom = p_datetime.day
        adjusted_dom = dom + first_day.weekday()

        unpadded: str = str(ceil(adjusted_dom / 7.0))
        return_var: str = str.rjust(unpadded, 2, '0')

        return return_var


    @classmethod
    def IntervalIDForName(cls,
                          p_interval_name: str) -> int:

        level_id_for_name: int = cls.NOTSET

        NAME_TO_INTERVAL_ID = {
            'MINUTE': cls.MINUTE,
            'HOUR': cls.HOUR,
            'DAY': cls.DAY,
            'WEEK': cls.WEEK,
            'MONTH': cls.MONTH,
            'YEAR': cls.YEAR,
            'NOTSET': cls.NOTSET, }

        try:
            level_id_for_name = NAME_TO_INTERVAL_ID[p_interval_name.upper().strip()]
        except Exception as e:
            print("Logging error in IntervalIDForName!:{}", e)

        return level_id_for_name


    @classmethod
    def NameForIntervalID(cls,
                          p_interval_level_id: int) -> str:

        name_for_level_id: str = 'NOTSET'

        INTERVAL_ID_TO_NAME = {
                cls.MINUTE: 'MINUTE',
                cls.HOUR: 'HOUR',
                cls.DAY: 'DAY',
                cls.WEEK: 'WEEK',
                cls.MONTH: 'MONTH',
                cls.YEAR: 'YEAR',
                cls.NOTSETET: 'NOTSET'}

        try:
            name_for_level_id = INTERVAL_ID_TO_NAME[p_interval_level_id]
        except Exception as e:
            print("Logging error in NameForIntervalID!:{}", e)

        return name_for_level_id



    @classmethod
    def CONSTANT_VALUE_LIST(cls):
        return [cls.MINUTE,
                cls.HOUR,
                cls.DAY,
                cls.WEEK,
                cls.MONTH,
                cls.YEAR,
                cls.NOTSET]

    @classmethod
    def CONSTANT_NAME_LIST(cls):
        return ['MINUTE',
                'HOUR',
                'DAY',
                'WEEK',
                'MONTH',
                'YEAR',
                'NOTSET']

    @classmethod
    def DateStringFromIntervalLevelID(cls,
                                      p_interval_level_id: int,
                                      p_current_time: datetime = datetime.now()) -> str:

        date_format_str = \
            {cls.MINUTE: "%Y%m%d-%H%M",
             cls.HOUR: "%Y%m%d-%H",
             cls.DAY: "%Y%m%d",
             cls.WEEK: "%Y%m",
             cls.MONTH: "%Y%m",
             cls.YEAR: "%Y",
             cls.NOTSET: "%Y%m%d-%H:%M:%S.%f"}

        date_string = p_current_time.strftime(date_format_str[p_interval_level_id])

        if p_interval_level_id == cls.WEEK:

            date_string += LOG_FILE_INTERVAL_C.__week_of_month(p_current_time)


        return date_string



class LOG_C(cu.Const):

    CRITICAL: int = logging.CRITICAL
    FATAL: int = logging.FATAL
    ERROR: int = logging.ERROR
    WARNING: int = logging.WARNING
    WARN: int = logging.WARNING
    INFO: int = logging.INFO
    DEBUG: int = logging.DEBUG
    NOTSET: int = logging.NOTSET



    @classmethod
    def LevelIDForName(cls,
                       p_level_name: str) -> int:

        level_id_for_name: int = cls.NOTSET

        NAME_TO_ID = {
            'CRITICAL': logging.CRITICAL,
            'FATAL': logging.FATAL,
            'ERROR': logging.ERROR,
            'WARN': logging.WARNING,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG,
            'NOTSET': logging.NOTSET, }

        try:
            level_id_for_name = NAME_TO_ID[p_level_name.upper().strip()]
        except Exception as e:
            print("Logging error in LevelIDForName!:{}", e)

        return level_id_for_name


    @classmethod
    def NameForLevelID(cls, p_level_id: int) -> str:

        name_for_level_id: str = 'NOTSET'

        ID_TO_NAME = \
            {cls.CRITICAL: 'CRITICAL',
             cls.FATAL: 'FATAL',
             cls.ERROR: 'ERROR',
             cls.WARNING: 'WARNING',
             cls.WARN: 'WARNING',
             cls.INFO: 'INFO',
             cls.DEBUG: 'DEBUG',
             cls.NOTSET: 'NOTSET'}

        try:
            name_for_level_id = ID_TO_NAME[p_level_id]
        except Exception as e:
            print("Logging error in NameForLevelID!:{}", e)

        return name_for_level_id


    @classmethod
    def DEFAULT_SCREEN_FORMAT_STRING(cls) -> str:

        str_format: str = "%(asctime)s|" \
                          "%(log_color)s%(levelname)-8s%(reset)s|" \
                          "%(process)d|%(thread)d |" \
                          "%(module)s|%(filename)s|%(lineno)d|" \
                          "%(blue)s%(message)s%(reset)s|" \
                          "%(purple)s%(args)s"
        return str_format


    @classmethod
    def DEFAULT_FILE_FORMAT_STRING(cls) -> str:

        str_format: str = "%(asctime)s|" \
                          "%(levelname)s|" \
                          "%(filename)s-%(lineno)d|" \
                          "%(message)s|" \
                          "%(args)s"

        return str_format


    @classmethod
    def CONSTANT_VALUE_LIST(cls):
        return [cls.CRITICAL,
                cls.FATAL,
                cls.ERROR,
                cls.WARNING,
                cls.WARN,
                cls.INFO,
                cls.DEBUG,
                cls.NOTSET]

    @classmethod
    def CONSTANT_NAME_LIST(cls):
        return ['CRITICAL',
                'FATAL',
                'ERROR',
                'WARNING',
                'WARN',
                'INFO',
                'DEBUG',
                'NOTSET']


class STAT_C(cu.Const):

    FATAL_ERROR = logging.FATAL
    CRITICAL_ERROR = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    OK = logging.NOTSET
    NOTSET = -1

    @classmethod
    def CONSTANT_VALUE_LIST(cls):
        return [cls.CRITICAL_ERROR,
                cls.FATAL_ERROR,
                cls.ERROR,
                cls.WARNING,
                cls.OK,
                cls.NOTSET]

    @classmethod
    def CONSTANT_NAME_LIST(cls):
        return ['CRITICAL_ERROR',
                'FATAL_ERROR',
                'ERROR',
                'WARNING',
                'OK',
                'NOTSET']



