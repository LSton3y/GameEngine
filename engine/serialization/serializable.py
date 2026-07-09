class Serializable:
    # Attributes which should be excluded from being serialized
    _exclude = set()


    # Converts class properties to dict
    def to_dict(self):
        return {
            key: value.to_dict() if hasattr(value, "to_dict") else value
            for key, value in self.__dict__.items()
            if key not in self._exclude
        }

    
    # Returns class created from data properties
    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)
        obj.__data__.update(data)
        return obj
