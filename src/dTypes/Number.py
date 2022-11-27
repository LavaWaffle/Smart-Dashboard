class Number:
    def __init__(self, key: str, value: int):
        self.key = key
        if not(type(value) is int or type(value) is float):
            raise TypeError("Value must be of type int or float")
        self.value = value

    def __init__(self, key: str, value: float):
        self.key = key
        if not(type(value) is int or type(value) is float):
            raise TypeError("Value must be of type int or float")
        self.value = value

    def get(self):
        return self.value

    def set(self, value: int):
        if not(type(value) is int or type(value) is float):
            raise TypeError("Value must be of type int or float")
        self.value = value