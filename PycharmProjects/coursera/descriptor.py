class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value-value*obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission