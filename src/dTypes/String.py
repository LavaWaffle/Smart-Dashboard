class String:
    def __init__(self, key: str, value: str):
        self.key = key
        if not(type(value) is str):
            raise TypeError("Value must be of type string")
        self.value = value

    def get(self):
        return self.value

    def set(self, value: str):
        if not(type(value) is str):
            raise TypeError("Value must be of type string")
        self.value = value