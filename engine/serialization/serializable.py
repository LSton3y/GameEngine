class Serializable:
    """
    Base class for objects that can be serialized to dictionaries.
    """

    # Attributes that shouldn't be saved
    _exclude = set()


    # Serializes a value into a dict
    @staticmethod
    def serialize(value):
        if hasattr(value, "to_dict"):
            return value.to_dict()

        if isinstance(value, list):
            return [Serializable.serialize(v) for v in value]

        if isinstance(value, dict):
            return {
                k.__name__ if isinstance(k, type) else k: Serializable.serialize(v)
                for k, v in value.items()
            }

        return value


    def to_dict(self):
        return {
            k: self.serialize(v)
            for k, v in self.__dict__.items()
            if k not in self._exclude
        }
            