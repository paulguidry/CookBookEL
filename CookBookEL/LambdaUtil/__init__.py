from abc import ABC, abstractmethod
import logging
from random import seed
from random import randint
import time
import sys
import os

RELATIVE_PATH: str = "/CEKitchenEL/ParameterUtil/__init__.py"

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())


try:

    import LogUtil as lu
    import LogUtil.LogWrapper as lw
    import LogUtil.HTTPStatusCodes as sc

except Exception as mnfe:
    import CookBookEL.LogUtil as lu
    import CookBookEL.LogUtil.LogWrapper as lw
    import CookBookEL.LogUtil.HTTPStatusCodes as sc




class LambdaHandlerRequest(object):
    """Base Request."""

    def __init__(self, event, context, **kwargs):
        """Initialize the request."""
        self.__event = event
        self.__context = context


    @property
    def event(self):
        """Return AWS Lambda Event Object."""
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value
        # return self.__event


    @property
    def context(self):
        """Return AWS Lambda Context Object."""
        return self.__context

    @context.setter
    def context(self, value):
        self.__context = value
        # return self.__context



class LambdaHandlerResponse:


    @property
    def StatusCode(self):
        return self.__status_code

    @StatusCode.setter
    def StatusCode(self, value):
        self.__status_code = value


    @property
    def StatusMsg(self):
        return self.__status_msg

    @StatusMsg.setter
    def StatusMsg(self, value):
        self.__status_msg = value


    @property
    def LambdaName(self) -> str:
        return self.__lambda_name

    @LambdaName.setter
    def LambdaName(self, value: str):
        self.__lambda_name = value


    @property
    def EventReturn(self) -> dict:
        return self.__event_return

    @EventReturn.setter
    def EventReturn(self, value: dict):
        self.__event_return = value


    @property
    def FullBody(self) -> dict:

        body_dict = {'statusCode': self.StatusCode,
                     'body': {'executed_lambda_with_name': self.LambdaName,
                              'event_return': self.EventReturn,
                              'status_message': self.StatusMsg}}

        return body_dict


    @property
    def serialized(self):

        return self.FullBody



    def __init__(self,
                 p_status_code: int,
                 p_status_msg: str,
                 p_lambda_name: str,
                 p_event_return):

        self.__status_code: int = p_status_code
        self.__status_msg: str = p_status_msg
        self.__lambda_name: str = p_lambda_name
        self.__event_return: dict = p_event_return






class LambdaHandlerBase(ABC):
    """Base Handler."""


    @property
    def Logger(self) -> logging:
        return self.__logger

    @Logger.setter
    def Logger(self, value: logging):
        self.__logger = value


    @property
    def StatusCode(self):
        return self.__status_code

    @StatusCode.setter
    def StatusCode(self, value):
        self.__status_code = value


    @property
    def StatusMsg(self):
        return self.__status_msg

    @StatusMsg.setter
    def StatusMsg(self, value):
        self.__status_msg = value


    @property
    def LambdaName(self) -> str:
        return self.__lambda_name

    @LambdaName.setter
    def LambdaName(self, value: str):
        self.__lambda_name = value


    @property
    def EventReturn(self) -> dict:
        return self.__event_return

    @EventReturn.setter
    def EventReturn(self, value: dict):
        self.__event_return = value



    def SimulateWorkDuration(self,
                             p_min_seconds: int,
                             p_max_seconds: int) -> int:

        time_to_pause = randint(p_min_seconds, p_max_seconds)
        time.sleep(time_to_pause)

        return time_to_pause


    def __SetUpLogging(self,
                       p_event: dict) -> logging:

        log_level_str = 'unknown'

        if p_event != {} and 'log_level_str' in p_event.keys():
            log_level_str = p_event['log_level_str']
        else:
            log_level_str = 'error'

        log_level_id: int = lw.LogWrapperClass.GetDebugLevelForName(log_level_str)

        self.__logger: logging = lw.LogWrapperClass(p_logger_name=self.LambdaName,
                                                    p_screen_log_level_id=log_level_id)

        self.Logger.info(f"Set log level", log_level=log_level_str)



    def __init__(self, **p_event):

        self.request_class = LambdaHandlerRequest
        self.request = None

        if p_event != {} and 'lambda_name' in p_event.keys():
            self.__lambda_name = p_event['lambda_name']
        else:
            self.__lambda_name = 'Not set'


        self.__status_code: int = sc.HTTP_RESTFULL_STATUS_CODES.NOT_SET
        self.__status_msg: str = sc.HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(sc.HTTP_RESTFULL_STATUS_DESC.NOT_SET)
        self.__event_return: dict = {}



    def DoWorkWrapper(self,
                      p_do_work_func: callable):

        try:
            p_do_work_func(self.request)

            if self.StatusCode == sc.HTTP_RESTFULL_STATUS_CODES.NOT_SET:
                self.StatusCode = sc.HTTP_RESTFULL_STATUS_CODES.OK
                self.StatusMsg = sc.HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(sc.HTTP_RESTFULL_STATUS_DESC.OK)

                temp_dict: dict = self.EventReturn
                temp_dict['lambda_name'] = self.LambdaName
                temp_dict['status_code'] = self.StatusCode
                temp_dict['status_msg'] = self.StatusMsg

                self.Logger.info('Work done successfully')

                self.Logger.debug('Data Returned From lambda:', **temp_dict)

        except AssertionError as ae:
            self.StatusMsg = sc.HTTP_RESTFULL_STATUS_CODES.SHORT_DESC(sc.HTTP_RESTFULL_STATUS_DESC.ASSERTION_ERROR)
            self.StatusCode = sc.HTTP_RESTFULL_STATUS_CODES.ASSERTION_ERROR
            self.Logger.critical(self.StatusMsg,
                                 error_msg=ae.args[0],
                                 formatted_exp=lu.format_exception(ae))

        except Exception as e:
            self.StatusMsg = sc.HTTP_RESTFULL_STATUS_CODES.SHORT_DESC \
                (sc.HTTP_RESTFULL_STATUS_DESC.TRAPPED_UNEXPECTED_ERROR)
            self.StatusCode = sc.HTTP_RESTFULL_STATUS_CODES.TRAPPED_UNEXPECTED_ERROR
            self.Logger.fatal(self.StatusMsg,
                              error_msg=e.args[0],
                              formatted_exp=lu.format_exception(e))




    def __call__(self, event, context, **kwargs):
        """Wrap dowork(), invoked by AWS Lambda."""
        self.__init__()  # reset the instance

        self.request = self.request_class(event, context)

        self.__SetUpLogging(p_event=event)

        self.DoWorkWrapper(p_do_work_func=self.DoWork)

        response = LambdaHandlerResponse(p_lambda_name=self.LambdaName,
                                         p_status_code=self.StatusCode,
                                         p_status_msg=self.StatusMsg,
                                         p_event_return=self.EventReturn)

        response.LambdaName = self.LambdaName

        return response.serialized


    @abstractmethod
    def DoWork(self, request, **kwargs):
        """Stub perform method."""
        raise NotImplementedError
