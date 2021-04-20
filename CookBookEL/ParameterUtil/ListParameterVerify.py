from abc import ABC
from typing import NamedTuple, Any
import re
import sys

from . __init__ import VerifiedParamReturnNT as vpr
from . __init__ import GenericParamVerificationClass as gpvc


class ListParamVerificationClass(gpvc):

    @property
    def MinNumberOfElements(self) -> int:
        return self.__min_number_of_elements


    @property
    def MaxNumberOfElements(self) -> int:
        return self.__max_number_of_elements


    @property
    def ElementVerificationClass(self) -> gpvc:
        return self.__element_verification_class


    def __init__(self,
                 p_key: Any,
                 p_element_verification_class: gpvc,
                 p_min_number_of_elements: int,
                 p_max_number_of_elements: int,
                 p_key_case_sensitive=False,
                 p_value_can_be_none: bool = False):

        gpvc.__init__(self,
                      p_key=p_key,
                      p_key_case_sensitive=p_key_case_sensitive,
                      p_value_can_be_none=p_value_can_be_none)

        self.__min_number_of_elements = p_min_number_of_elements
        self.__max_number_of_elements = p_max_number_of_elements
        self.__element_verification_class = p_element_verification_class


    def VerifyListElementsRtrnDictOfFailures(self, p_value: []) -> dict:

        return_dict = dict()

        for k, v in enumerate(p_value):
            val = self.ElementVerificationClass.ExtractAndVerifyValueFromDict(p_target_dict={'column': v})
            if not val.param_value_valid:
                return_dict[v] = val

        return return_dict





    def VerifyValue(self,
                    p_value: any) -> (bool, str):


        is_extracted_value_valid, validation_reason = gpvc.VerifyValue(self, p_value)

        if is_extracted_value_valid and p_value is not None:

            if not isinstance(p_value, list):
                is_extracted_value_valid = False
                validation_reason = f"Value ({p_value}) is not a list"

            elif self.MinNumberOfElements > len(p_value):
                is_extracted_value_valid = False
                validation_reason = "length of parameter value " \
                                    f"'{len(p_value)}'" \
                                    f" is shorter than ({self.MinNumberOfElements})!"

            elif 0 < self.MaxNumberOfElements < len(p_value):
                is_extracted_value_valid = False
                validation_reason = "length of parameter value " \
                                    f"'{len(p_value)}'" \
                                    f" is larger than ({self.MaxNumberOfElements})!"
            else:
                    pass
        else:
            pass

        if is_extracted_value_valid:
            invalid_elements: dict = self.VerifyListElementsRtrnDictOfFailures(p_value)

            if invalid_elements != dict():
                is_extracted_value_valid = False
                validation_reason = str(invalid_elements)

        return is_extracted_value_valid, validation_reason
