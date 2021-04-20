import logging
import timeit
import traceback
from datetime import datetime
from functools import wraps
from typing import Any
from envyaml import EnvYAML
from colorlog import ColoredFormatter
import sys
from pathlib import Path
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

if Path(os.getcwd()).parent not in sys.path:
    sys.path.append(Path(os.getcwd()).parent)

if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)

if Path(__file__) not in sys.path:
    sys.path.append(Path(__file__))

print('paul', os.getcwd())
print('guidry',sys.path)




try:
    from LogUtil import LOG_C, STAT_C, LOG_FILE_INTERVAL_C
    import LogUtil as lu
except Exception as mnfe:
    import CookBookEL.LogUtil as lu
    from CookBookEL.LogUtil import LOG_C, STAT_C, LOG_FILE_INTERVAL_C




class UnrecoverableError(Exception):

    def __init__(self,
                 p_name_of_error_source: str,
                 p_message="Unrecoverable Error Occurred!"):
        self.name_of_error_source = p_name_of_error_source
        self.message = p_message
        super().__init__(self.message)

    def __str__(self):
        val_dict = {'Name Of Source': self.name_of_error_source, 'Error Desc': self.message}
        return str(val_dict)



class LogWrapperClass(object):

    @property
    def ExecutionStatusId(self) -> int:
        return self.__execution_status_id
    
    @ExecutionStatusId.setter
    def ExecutionStatusId(self, p_value: int):
        assert(p_value in STAT_C.CONSTANT_VALUE_LIST())
        self.__execution_status_id = p_value

    @property
    def LoggerName(self) -> str:
        return self.__logger_name

    @property
    def ScreenLogLevelId(self) -> int:
        return self.__screen_log_level_id

    @property
    def FileLogLevelId(self) -> int:
        return self.__file_log_level_id

    @property
    def ScreenLogFormatStr(self) -> str:
        return self.__screen_log_format_str

    @property
    def FileLogFormatStr(self) -> str:
        return self.__file_log_format_str

    @property
    def LogFileDirUrl(self) -> str:
        return self.__log_file_dir_url

    @property
    def FileLifetimeIntervalId(self) -> int:
        return self.__file_lifetime_interval_id


    def debug(self, p_message: str, **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.debug(p_message)
        else:
            self.__logger.debug(p_message, p_extra)


    def info(self, p_message: str, **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.info(p_message)
        else:
            self.__logger.info(p_message, p_extra)


    def warning(self, p_message: str, **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.warning(p_message)
        else:
            self.__logger.warning(p_message, p_extra)


    def error(self, p_message: str, **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.error(p_message)
        else:
            self.__logger.error(p_message, p_extra)


    def critical(self, p_message: str, **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.critical(p_message)
        else:
            self.__logger.critical(p_message, p_extra)


    def fatal(self, p_message: str,  **p_extra) -> None:
        if p_extra is None or p_extra == {}:
            self.__logger.fatal(p_message)
        else:
            self.__logger.fatal(p_message, p_extra)


    def logit(self,
              p_message: str,
              p_log_level: int,
              **p_extra) -> None:
        if p_log_level == LOG_C.DEBUG:
            self.debug(p_message, **p_extra)
        elif p_log_level == LOG_C.INFO:
            self.info(p_message, **p_extra)
        elif p_log_level == LOG_C.ERROR:
            self.error(p_message, **p_extra)
        elif p_log_level == LOG_C.WARNING:
            self.warning(p_message, **p_extra)
        elif p_log_level == LOG_C.CRITICAL:
            self.critical(p_message, **p_extra)
        elif p_log_level == LOG_C.FATAL:
            self.fatal(p_message, **p_extra)





    def __SetUpLogging(self):

        log: logging.Logger = logging.getLogger(self.__logger_name)

        log.setLevel(LOG_C.DEBUG)  # set all logging at the handler level

        if self.ScreenLogLevelId != LOG_C.NOTSET:
            sth = logging.StreamHandler()
            sth.setLevel(self.ScreenLogLevelId)
            formatter = ColoredFormatter(LOG_C.DEFAULT_SCREEN_FORMAT_STRING(),
                                         log_colors={'DEBUG':    'cyan',
                                                     'INFO':     'green',
                                                     'WARNING':  'yellow',
                                                     'ERROR':    'yellow,bg_purple',
                                                     'CRITICAL': 'red,bg_yellow'})
            
            sth.setFormatter(formatter)
            log.addHandler(sth)

        if self.FileLogLevelId != LOG_C.NOTSET:
            log_start_time = datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")
            full_log_url = str.format("{}{}{}{}.log",
                                      self.LogFileDirUrl,
                                      os.sep,
                                      self.LoggerName,
                                      log_start_time)
            file_object = open(full_log_url, 'a')
            file_object.write('-'.join([char * 80 for char in '-']))
            file_object.write("\n")
            file_object.write(self.LoggerName + " ------------ ")
            file_object.write(datetime.now().strftime("%d %b %y %H:%M:%S.%f"))
            file_object.write("\n")
            file_object.write('-'.join([char * 80 for char in '-']))
            file_object.write("\n")
            file_object.close()

            fhnd = logging.FileHandler(full_log_url)
            fhnd.setLevel(self.FileLogLevelId)
            formatter = logging.Formatter(LOG_C.DEFAULT_FILE_FORMAT_STRING())
            fhnd.setFormatter(formatter)
            log.addHandler(fhnd)

        return log


    @classmethod
    def GetDebugLevelForName(cls,
                             p_log_level_name: str) -> int:

        assert p_log_level_name.strip().upper() in LOG_C.CONSTANT_NAME_LIST(), \
            f'Unknown debug level received ({p_log_level_name}. ' \
            f'Valid options are ({str(LOG_C.CONSTANT_NAME_LIST())}))'

        return LOG_C.LevelIDForName(p_log_level_name.strip().upper())


    @classmethod
    def InitWithYamlFile(cls,
                         p_logger_name: str,
                         p_yaml_config_obj: EnvYAML):

        assert (p_yaml_config_obj is not None), "The yaml config object sent is null!"
        logger_name: str = p_logger_name

        screen_format_str: str = p_yaml_config_obj['screen.log_format_str']
        screen_log_level_name: str = p_yaml_config_obj['screen.log_level_name']

        file_log_level_name: str = p_yaml_config_obj['file_log.log_level_name']
        file_log_format_str: str = p_yaml_config_obj['file_log.format_str']
        file_log_dir_url: str = p_yaml_config_obj['file.log_dir_url']

        return cls.InitWithLogLevelNames(p_logger_name=logger_name,
                                         p_screen_log_format_str=screen_format_str,
                                         p_screen_log_level_name=screen_log_level_name,
                                         p_file_log_level_name=file_log_level_name,
                                         p_file_log_format_str=file_log_format_str,
                                         p_file_log_dir_url=file_log_dir_url)


    @classmethod
    def InitWithLogLevelNames(cls,
                              p_logger_name: str,
                              p_file_lifetime_interval_name='NOTSET',
                              p_file_log_dir_url: str = 'NOTSET',
                              p_file_log_format_str: str = LOG_C.DEFAULT_FILE_FORMAT_STRING(),
                              p_file_log_level_name: str = 'NOTSET',
                              p_screen_log_format_str: str = LOG_C.DEFAULT_SCREEN_FORMAT_STRING(),
                              p_screen_log_level_name: str = 'NOTSET'):

        assert (p_file_log_level_name.upper().strip() in LOG_C.CONSTANT_NAME_LIST()), \
            str.format("Log level name ({}), not valid [{}]",
                       p_file_log_level_name,
                       LOG_C.CONSTANT_VALUE_LIST())
        file_log_level_name_id = LOG_C.LevelIDForName(p_file_log_level_name)

        assert (p_screen_log_level_name.upper().strip() in LOG_C.CONSTANT_NAME_LIST()), \
            str.format("Log level name ({}), not valid [{}]",
                       p_screen_log_level_name, LOG_C.CONSTANT_VALUE_LIST())
        screen_log_level_id = LOG_C.LevelIDForName(p_screen_log_level_name)

        assert (p_file_lifetime_interval_name.upper().strip() in LOG_FILE_INTERVAL_C.CONSTANT_NAME_LIST()), \
            str.format("Log lifetime interval name ({}), not valid [{}]",
                       p_file_lifetime_interval_name,
                       LOG_FILE_INTERVAL_C.CONSTANT_NAME_LIST())

        file_lifetime_interval_id = LOG_FILE_INTERVAL_C.IntervalIDForName(p_file_lifetime_interval_name)

        return cls(p_logger_name=p_logger_name,
                   p_file_lifetime_interval_id=file_lifetime_interval_id,
                   p_file_log_dir_url=p_file_log_dir_url,
                   p_file_log_format_str=p_file_log_format_str,
                   p_file_log_level_id=file_log_level_name_id,
                   p_screen_log_format_str=p_screen_log_format_str,
                   p_screen_log_level_id=screen_log_level_id)


    def __init__(self,
                 p_logger_name: str,
                 p_file_lifetime_interval_id: int = LOG_FILE_INTERVAL_C.NOTSET,
                 p_file_log_dir_url: str = 'NOTSET',
                 p_file_log_format_str: str = LOG_C.DEFAULT_FILE_FORMAT_STRING(),
                 p_file_log_level_id: int = LOG_C.NOTSET,
                 p_screen_log_format_str: str = LOG_C.DEFAULT_SCREEN_FORMAT_STRING(),
                 p_screen_log_level_id: int = LOG_C.ERROR):

        # LOGGER NAME
        assert (p_logger_name is not None and len(p_logger_name.strip()) >= 4), \
            str.format("invalid logger name ({}) not acceptable! Must be at least 4 chars.", p_logger_name)
        self.__logger_name: str = p_logger_name

        # SCREEN LOG LEVEL
        assert(p_screen_log_level_id in LOG_C.CONSTANT_VALUE_LIST()), \
            str.format('Invalid screen log level id ({}). valid values are ({})',
                       p_screen_log_level_id,
                       LOG_C.CONSTANT_VALUE_LIST())
        self.__screen_log_level_id: int = p_screen_log_level_id

        # SCREEN LOG LEVEL FORMAT
        if self.__screen_log_level_id != LOG_C.NOTSET:
            assert (p_screen_log_format_str is not None and len(p_screen_log_format_str.strip()) >= 4), \
                str.format("invalid string format ({})! Must be at least 4 chars.", p_screen_log_format_str)
            self.__screen_log_format_str: str = p_screen_log_format_str

        # FILE LOG LEVEL FORMAT
        assert(p_file_log_level_id in LOG_C.CONSTANT_VALUE_LIST()), \
            str.format('Invalid file log level id ({}). valid values are ({})',
                       p_file_log_level_id,
                       LOG_C.CONSTANT_VALUE_LIST())
        self.__file_log_level_id: int = p_file_log_level_id

        # FILE LOG FORMAT STRING
        if self.__file_log_level_id != LOG_C.NOTSET:
            assert (p_file_log_format_str is not None and len(p_file_log_format_str.strip()) >= 4), \
                str.format("invalid string format ({})! Must be at least 4 chars.", p_file_log_format_str)
            self.__file_log_format_str: str = p_file_log_format_str \

            # FILE LOG DIRECTORY URL
            assert (p_file_log_dir_url is not None and len(p_file_log_dir_url.strip()) >= 4), \
                str.format("invalid file_log_dir_url ({}) not acceptable! Must be at least 4 chars.", p_logger_name)

            self.__log_file_dir_url: str = p_file_log_dir_url

        # LOG FILE_INTERVAL
        self.__file_lifetime_interval_id: int = p_file_lifetime_interval_id

        # EXECUTION STATUS
        self.__execution_status_id: int = STAT_C.NOTSET

        # SET UP LOGGING
        self.__logger: logging.Logger = self.__SetUpLogging()


    @staticmethod
    def CriticalErrorHandeler(p_status_on_success: int,
                              p_status_on_error: int):

        def inner_function(function, **kwargs):

            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                function_return: [] = list(function(cls, *args, **kwargs))
                status: int = function_return.pop(0)

                cls.StatusCode = p_status_on_success

                if status == STAT_C.OK:
                    cls.StatusCode = p_status_on_success
                else:
                    cls.StatusCode = p_status_on_error
                    raise UnrecoverableError(p_name_of_error_source=function.__qualname__)

                return *function_return,

            return wrapper

        return inner_function


    @staticmethod
    def FunctWrapNoReturn(p_func_log_level: int,
                          p_function_error_log_level=LOG_C.ERROR):

        def inner_function(function, **kwargs):

            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                status_code: int = STAT_C.NOTSET
                try:
                    cls.Log.logit(str.format("Executing function ({})",
                                             function.__qualname__), p_func_log_level)
                    start = timeit.default_timer()
                    function(cls, *args, **kwargs)
                    stop = timeit.default_timer()
                    execution_time = (stop - start)
                    cls.Log.logit(p_message=str.format("Executed successfully function ({})",
                                                       function.__qualname__),
                                  p_log_level=p_func_log_level,
                                  p_extra={'runtime(ms)': execution_time})

                    status_code = STAT_C.OK

                except Exception as e:
                    status_desc: str = traceback.format_exc()
                    cls.Log.logit(str.format("Execute ERROR function ({}) - {}",
                                             function.__qualname__, status_desc), p_function_error_log_level)

                finally:
                    return status_code,

            return wrapper

        return inner_function


    @staticmethod
    def FunctWrapOneReturn(p_func_log_level: int,
                           p_function_error_log_level=LOG_C.ERROR):

        def inner_function(function, **kwargs):

            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                function_return: Any = None
                status_code: int = STAT_C.NOTSET
                try:
                    cls.Log.logit(str.format("Executing function ({})",
                                             function.__qualname__), p_func_log_level)
                    start = timeit.default_timer()
                    function_return = function(cls, *args, **kwargs)
                    stop = timeit.default_timer()
                    execution_time = (stop - start)
                    cls.Log.logit(p_message=str.format("Executed successfully function ({})",
                                                       function.__qualname__),
                                  p_log_level=p_func_log_level,
                                  p_extra={'runtime(ms)': execution_time})

                    status_code = STAT_C.OK

                except Exception as e:
                    status_desc: str = traceback.format_exc()
                    cls.Log.logit(str.format("Execute ERROR function ({}) - {}",
                                             function.__qualname__, status_desc), p_function_error_log_level)
                    status_code = STAT_C.ERROR
                finally:
                    return status_code, function_return

            return wrapper

        return inner_function


    @staticmethod
    def FunctWrapMultiReturn(p_func_log_level: int,
                             p_function_error_log_level=LOG_C.ERROR):

        def inner_function(function, **kwargs):

            @wraps(function)
            def wrapper(cls, *args, **kwargs):
                function_return: [] = []
                status_code: int = STAT_C.NOTSET
                try:
                    cls.Log.logit(str.format("Executing function ({})",
                                             function.__qualname__), p_func_log_level)

                    start = timeit.default_timer()
                    function_return = function(cls, *args, **kwargs)
                    stop = timeit.default_timer()
                    execution_time = (stop - start)
                    cls.Log.logit(p_message=str.format("Executed successfully function ({})",
                                                       function.__qualname__),
                                  p_log_level=p_func_log_level,
                                  p_extra={'runtime(ms)': execution_time})

                    status_code = STAT_C.OK

                except Exception as e:
                    status_desc: str = traceback.format_exc()
                    cls.Log.logit(str.format("Execute ERROR function ({}) - {}",
                                             function.__qualname__, status_desc), p_function_error_log_level)
                finally:
                    return status_code, *function_return

            return wrapper

        return inner_function


if __name__ == '__main__':

    ll = LogWrapperClass(p_logger_name='__name__',
                         p_screen_log_level_id=LOG_C.DEBUG)
    ll.info('was here', extra=__name__)

    '''
    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)

    # %%
    import inspect

    frame=inspect.stack()[0]
    print(len(inspect.stack()))
    print(inspect.getmodule(frame[0]))


    print(os.getcwd())


    import logging

    LOG_LEVEL=logging.DEBUG
    LOGFORMAT="%(asctime)s|%(log_color)s%(levelname)-8s%(reset)s|%(filename)s-%(lineno)d|%(log_color)s%(message)s%(reset)s|%(args)s"
    from colorlog import ColoredFormatter

    logging.root.setLevel(LOG_LEVEL)
    formatter=ColoredFormatter(LOGFORMAT)
    stream=logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)
    log=logging.getLogger('pythonConfig')
    log.setLevel(LOG_LEVEL)
    log.addHandler(stream)

    log.debug("A quirky message only developers care about")
    log.info("Curious users might want to know this")
    log.warning("Something is wrong and any user should be informed")
    log.error("Serious stuff, this is red for a reason",{'Reason':__file__})
    log.critical("OH NO everything is on fire")
    '''
