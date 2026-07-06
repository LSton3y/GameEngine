class SingletonMeta(type):
    """
    Metaclass used to create singleton classes
    
    Use instance() to call class instance
    """

    _instances = {} # Stores singleton instances


    # Called every time the class is called, e.g. Class()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


    # Returns class instance
    def instance(cls):
        if cls not in cls._instances:
            raise RuntimeError(f"{cls.__name__} has not been created yet")
        return cls._instances[cls]
