class Singleton:
    """
    Super class used to create singleton classes

    Use 'super().__init__(cls)' in sub classes initialization
    """
    _instance = None


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    @classmethod
    def instance(cls):
        if cls._instance is None:
          raise ValueError(f"{cls.__name__} singleton does not exist.")
        return cls._instance