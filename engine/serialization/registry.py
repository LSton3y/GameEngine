class Registry:
    """
    Handles the registry of components
    """
    _registry = {}


    @staticmethod
    def register(cls):
        Registry._registry.add(cls.__name__)
    
    
    @staticmethod
    def get(name):
        return Registry._registry.get(name)