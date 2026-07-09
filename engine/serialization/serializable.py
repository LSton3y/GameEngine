class Serializable:
    """
    Base class for objects that can be serialized to dictionaries.
    """

    # Attributes that shouldn't be saved
    _exclude = set()


    def to_dict(self):
        data = {}

        for key, value in self.__dict__.items():
            if key in self._exclude:
                continue

            if hasattr(value, "to_dict"):
                data[key] = value.to_dict()
            else:
                data[key] = value

        return data


    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)

        for key, value in data.items():
            setattr(obj, key, value)

        return obj