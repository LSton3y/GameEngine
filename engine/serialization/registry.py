class Registry:
    """
    Handles the registry of components
    """
    _registry = {}


    @staticmethod
    def register(cls):
        Registry._registry[cls.__name__] = cls
    

    @staticmethod
    def get(name):
        return Registry._registry.get(name)