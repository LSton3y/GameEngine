class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    def instance(cls):
        if cls not in cls._instances:
            raise RuntimeError(f"{cls.__name__} has not been created yet")
        return cls._instances[cls]
