class Boolean:
    def __init__(self, key: str, value: bool):
        self.key = key
        if not(type(value) is bool):
            raise TypeError("Value must be of type bool")
        self.value = value

    def get(self):
        return self.value

    def set(self, value: bool):
        if not(type(value) is bool):
            raise TypeError("Value must be of type bool")
        self.value = value