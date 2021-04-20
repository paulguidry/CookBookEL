from abc import ABCMeta, abstractmethod


class ConstantTypeError(Exception):

    def __init__(self,
                 p_name,
                 p_new_value,
                 p_message="Constant value cannot be changed!"):

        self.name = p_name
        self.message = p_message
        self.new_value = p_new_value

        super().__init__(self.message)


    def __str__(self):

        val_dict: dict = {"Var-name": self.name,
                          "new-value": self.new_value,
                          "constant value error": self.message}

        return str(val_dict)



class __MetaConst(type, metaclass=ABCMeta):

    def __getattr__(cls, p_key):
        return cls[p_key]

    def __setattr__(cls, p_key, p_value):
        raise ConstantTypeError(p_name=p_key, p_new_value=p_value)



class Const(object, metaclass=__MetaConst):

    @classmethod
    @abstractmethod
    def CONSTANT_NAME_LIST(cls):
        pass


    @classmethod
    @abstractmethod
    def CONSTANT_VALUE_LIST(cls):
        pass

    def __getattr__(self, p_name):
        return self[p_name]

    def __setattr__(self, p_name, p_value):
        raise ConstantTypeError(p_name=p_name, p_new_value=p_value)


    @classmethod
    def ConstantNameInList(cls, p_value) -> bool:
        cont_in_list: bool = p_value in cls.CONSTANT_NAME_LIST()
        return cont_in_list

    @classmethod
    def ConstantValueInList(cls, p_value) -> bool:
        cont_in_list: bool = p_value in cls.CONSTANT_VALUE_LIST()
        return cont_in_list



if __name__ == "__main__":

    class MyConst(Const):
        A = 1
        B = 2

        @classmethod
        def CONSTANT_VALUE_LIST(cls):
            return [cls.A, cls.B]

        @classmethod
        def CONSTANT_NAME_LIST(cls):
            return ['A', 'B']


    try:
        MyConst.A = "changed"
    except Exception as e:
        print(e)

    my_const = MyConst()

    print(MyConst.ConstantValueInList(7))

    try:
        my_const.A = "changed"
    except Exception as e:
        print(e)
        # raise(e)
