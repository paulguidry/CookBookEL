from typing import NamedTuple, Any
from abc import ABC, abstractmethod
import sys
import os

RELATIVE_PATH: str = "/CEKitchenEL/ParameterUtil/__init__.py"

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

try:
    import ConstantUtil as cu
except Exception as e:
    from CookBookEL import ConstantUtil as cu


class VerifiedParamReturnNT(NamedTuple):
    """
    : parameter_found: The event dictionary of parameters sent to lambda!
    :return: tuple: key_name - The name of the parameter
                    parameter_found - True if the parameter was found
                    parameter_value_valid - True if the parameter value is valid
                    used_default_value - if default value was used in place of a missing value
                    parameter_value - if parameter_found should be set to default value if exist
                    validation_reason - A desciption of how the parameter was validated
    """
    key_name: str = ''
    param_found: bool = False
    param_value_valid: bool = False
    used_default_value: bool = False
    param_value: Any = str()
    validation_reason: str = ""




class ParamVerificationClass(ABC):

    @property
    @abstractmethod
    def DefaultValue(self):
        """Should never reach this. Needs to be implemented from Child class"""
        raise NotImplementedError


    @property
    def KeyDatatypeName(self) -> str:
        return self.__key_data_type_name


    @property
    def KeyCaseSensitive(self) -> bool:
        return self.__key_case_sensitive


    @property
    def Key(self) -> Any:
        return self.__key


    @abstractmethod
    def VerifyValue(self,
                    p_value: any) -> (bool, str):
        """Should never reach this. Needs to be implemented from Child class"""
        raise NotImplementedError


    def ExtractValueFromDict(self, p_target_dict: dict) -> Any:

        return_value: Any = None
        found_key: Any = None

        if self.KeyDatatypeName == 'str':
            found_key = self.__SearchDictForMatchingStrKey(p_target_dict)
            found_key = None if found_key == '' else found_key
        elif self.KeyDatatypeName == 'int':
            found_key = self.Key if self.__DoesMatchingIntKeyExist(p_target_dict) else None
        else:
            """Should never reach this"""
            raise NotImplementedError

        if found_key is not None:
            return_value = p_target_dict[self.Key]
        else:
            raise KeyError(f"The key '{self.Key}' was not found in the given dict!")

        return return_value



    def ExtractAndVerifyValueFromDict(self, p_target_dict: dict) -> VerifiedParamReturnNT:

        return_var: Any

        try:

            extracted_value = self.ExtractValueFromDict(p_target_dict=p_target_dict)

            is_extracted_value_valid, validation_reason = self.VerifyValue(p_value=extracted_value)


            return_var = VerifiedParamReturnNT \
                             (key_name=self.Key,
                              param_found=True,
                              param_value_valid=is_extracted_value_valid,
                              used_default_value=False,
                              param_value=extracted_value,
                              validation_reason=validation_reason)


        except KeyError as ke:

            return_var = VerifiedParamReturnNT\
                              (key_name=self.Key,
                               param_found=False,
                               param_value_valid=(self.DefaultValue is not None),
                               used_default_value=(self.DefaultValue is not None),
                               param_value=self.DefaultValue,
                               validation_reason="Could Not Find Key. "
                                                 f"{'Used default' if self.DefaultValue is not None else ''}")


        return return_var



    def __init__(self,
                 p_key: Any,
                 p_key_case_sensitive: bool = True):
        """
        Default Constructor
        :param p_key: The key to look for.
        :param p_key_case_sensitive: If the datatype of the key is a string, do a case insensitive search.
        """

        assert isinstance(p_key, str) or \
               isinstance(p_key, int), \
               "'Data type of key was {type(p_key)}', bUt it be either a str or int datatype!"


        if isinstance(p_key, str):
            self.__key_data_type_name = 'str'
            self.__key_case_sensitive: bool = p_key_case_sensitive
            if not self.__key_case_sensitive:
                self.__key: str = p_key.lower().strip()
            else:
                self.__key: str = p_key

            assert self.__key is not None and self.__key != '' \
                f"key value '{self.__key}' can not be None Nor equal to '' !"

        elif isinstance(p_key, int):
            self.__key: int = p_key
            self.__key_data_type_name = 'int'
            self.__key_case_sensitive: bool = False

        else:
            """Should never reach this"""
            raise NotImplementedError



    def __SearchDictForMatchingStrKey(self,
                                      p_target_dict: dict) -> str:

        key_found: str = ''

        if not self.KeyCaseSensitive:
            for key in p_target_dict.keys():
                if self.Key == str(key).strip().lower():
                    key_found = key

        elif self.Key in p_target_dict.keys():
            key_found = self.Key

        return key_found


    def __DoesMatchingIntKeyExist(self,
                                  p_target_dict: dict) -> bool:

        key_found: bool = self.Key in p_target_dict.keys()

        return key_found




class GenericParamVerificationClass(ParamVerificationClass):


    @property
    def DefaultValue(self) -> bool:
        return self.__default_value


    @property
    def ListOfPossibleValues(self) -> tuple:
        return self.__list_of_possible_values


    @property
    def ValueCanBeNone(self) -> bool:
        return self.__value_can_be_None



    def VerifyValue(self,
                    p_value) -> (bool, str):

        validation_reason: str = ''
        is_extracted_value_valid: bool = False

        if p_value is None and not self.ValueCanBeNone:
            is_extracted_value_valid = False
            validation_reason = "The value found is None without 'ValueCanBeNone' set to true"

        elif p_value is None and self.ValueCanBeNone:
            is_extracted_value_valid = True
            validation_reason = "The value found is None with 'ValueCanBeNone' set to true"

        elif len(self.ListOfPossibleValues) > 0 and p_value not in self.ListOfPossibleValues:
            is_extracted_value_valid = False
            validation_reason = f"The value found '{p_value}' not in list of " \
                                f"possible values {str(self.ListOfPossibleValues)}!"

        else:
            is_extracted_value_valid = True
            validation_reason = "Passed all validations."


        return is_extracted_value_valid, validation_reason



    def __init__(self,
                 p_key: Any,
                 p_default_value: Any = None,
                 p_list_of_possible_values: tuple = (),
                 p_value_can_be_none: bool = False,
                 p_key_case_sensitive: bool = True):

        ParamVerificationClass.__init__(self,
                                        p_key,
                                        p_key_case_sensitive)

        self.__default_value: Any = p_default_value
        self.__list_of_possible_values: tuple = p_list_of_possible_values
        self.__value_can_be_None: bool = p_value_can_be_none




if __name__ == '__main__':

    print("test 1 - integer keys")

    pvc = GenericParamVerificationClass(p_key=17)
    assert pvc.Key == 17 and pvc.KeyDatatypeName == 'int' and pvc.KeyCaseSensitive is False

    test_val = pvc.ExtractValueFromDict(p_target_dict={17: '23456',
                                                       'Name': 'Paul'})
    assert test_val == 17

    rslt = pvc.ExtractAndVerifyValueFromDict(p_target_dict={17: '23456', 'Name': 'Paul'})

    assert rslt.key_name == 17 \
           and rslt.param_found \
           and rslt.param_value == 17 \
           and rslt.param_value_valid \
           and not rslt.used_default_value

    try:
        test_val = pvc.ExtractValueFromDict(p_target_dict={16: '23456',
                                                           'Name': 'Paul'})
    except KeyError as e:
        """ expected exception """

    rslt = pvc.ExtractAndVerifyValueFromDict(p_target_dict={16: '23456', 'Name': 'Paul'})

    assert rslt.key_name == 17 \
           and not rslt.param_found \
           and rslt.param_value is None \
           and not rslt.param_value_valid \
           and not rslt.used_default_value




    print("test 2 - string keys")

    pvc = GenericParamVerificationClass(p_key="17")
    assert pvc.Key == "17" and pvc.KeyDatatypeName == 'str' and pvc.KeyCaseSensitive is True

    test_val = pvc.ExtractValueFromDict(p_target_dict={"17": '23456',
                                                       'Name': 'Paul'})
    assert test_val == "17"

    try:
        test_val = pvc.ExtractValueFromDict(p_target_dict={16: '23456',
                                                           'Name': 'Paul'})
    except KeyError as e:
        """ expected exception """

    print("test complete")



