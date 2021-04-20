from typing import Any
import re
import os
import sys


if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())


try:
    import ConstantUtil as cu
    from . import GenericParamVerificationClass as gpvc
except Exception as e:
    from __init__ import GenericParamVerificationClass as gpvc
    from CookBookEL import ConstantUtil as cu



class StringParamVerificationClass(gpvc):

    @property
    def MinStrLength(self) -> int:
        return self.__min_str_length


    @property
    def MaxStrLength(self) -> int:
        return self.__max_str_length


    @property
    def RegExStr(self) -> str:
        return self.__regex_str


    def VerifyValue(self,
                    p_value: any) -> (bool, str):


        is_extracted_value_valid, validation_reason = gpfc.VerifyValue(self, p_value)

        if is_extracted_value_valid and p_value is not None:

            if not isinstance(p_value, str):
                is_extracted_value_valid = False
                validation_reason = f"Value ({p_value}) is not a String"

            elif self.MinStrLength > len(p_value):
                is_extracted_value_valid = False
                validation_reason = "length of parameter value " \
                                    f"'{len(p_value)}'" \
                                    f" is shorter than ({self.MinStrLength})!"

            elif 0 < self.MaxStrLength < len(p_value):
                is_extracted_value_valid = False
                validation_reason = "length of parameter value " \
                                    f"'{len(p_value)}'" \
                                    f" is larger than ({self.MaxStrLength})!"
            if self.RegExStr != '':
                match = re.search(self.RegExStr, p_value)
                if match:
                    is_extracted_value_valid = True
                    validation_reason = f"found {match.group()} using {self.RegExStr} " \
                                        f"on {p_value}!"
                else:
                    is_extracted_value_valid = False
                    validation_reason = f"Using {self.RegExStr} " \
                                        f"on {p_value} was false!"

            else:
                    pass

        else:
            pass

        return is_extracted_value_valid, validation_reason



    def __init__(self,
                 p_key: Any,
                 p_default_value: Any = None,
                 p_list_of_possible_values: tuple = (),
                 p_value_can_be_none: bool = False,
                 p_key_case_sensitive: bool = True,
                 p_min_str_length: int = -1,
                 p_max_str_length: int = -1,
                 p_regex_str: str = ''):

        gpfc.__init__(self,
                      p_key,
                      p_default_value,
                      p_list_of_possible_values,
                      p_value_can_be_none,
                      p_key_case_sensitive)

        self.__min_str_length = p_min_str_length
        self.__max_str_length = p_max_str_length
        self.__regex_str = p_regex_str





