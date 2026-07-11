class Singleton:
    """
    Super class used to create singleton classes

    Use 'super().__init__(cls)' in sub classes initialization
    """
    _instance = None


    def __init__(self, cls):
        if cls._instance is not None:
            raise ValueError("Class instance already exists.")
        else:
            cls._instance = self
  
    @classmethod
    def get_instance(cls):
        return cls._instance