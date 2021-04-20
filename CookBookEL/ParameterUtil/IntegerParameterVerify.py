from typing import Any
import sys


try:
    import ConstantUtil as cu
    from . import GenericParamVerificationClass as gpvc

except Exception as e:
    from CookBookEL import ConstantUtil as cu
    from __init__ import GenericParamVerificationClass as gpvc


class IntegerParamVerificationClass(gpvc):

    @property
    def DefaultMaxIntegerValue(self) -> int:
        return sys.maxsize

    @property
    def DefaultMinIntegerValue(self) -> int:
        return sys.maxsize*-1


    @property
    def MinIntegerValue(self) -> int:
        return self.__min_str_length


    @property
    def MaxIntegerValue(self) -> int:
        return self.__max_str_length



    def VerifyValue(self,
                    p_value: any) -> (bool, str):

        is_extracted_value_valid, validation_reason = gpvc.VerifyValue(self, p_value)

        if not isinstance(p_value, int):
            is_extracted_value_valid = False
            validation_reason = f"Value ({p_value}) is not a Integer!"

        elif is_extracted_value_valid:

            if not (self.MinIntegerValue <=
                    p_value <= self.MaxIntegerValue):
                is_extracted_value_valid = False
                validation_reason = "Parameter value " \
                                    f"({p_value}) " \
                                    f" not between ({self.MinIntegerValue}) and ({self.MaxIntegerValue})!"

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
                 p_max_integer=sys.maxsize,
                 p_min_integer=-1*sys.maxsize):

        gpvc.__init__(self,
                      p_key,
                      p_default_value,
                      p_list_of_possible_values,
                      p_value_can_be_none,
                      p_key_case_sensitive)

        self.__min_str_length = p_min_integer
        self.__max_str_length = p_max_integer






