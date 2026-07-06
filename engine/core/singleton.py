class Singleton:

    def __new__(cls, *args, **kwargs):
        # Create new singleton instance
        if cls._instance == None:
            cls._instance = super.__new__(cls)
        else:
            return # Return if instance already exists

        return cls._instance


    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise RuntimeError(f"{cls.__name__} has not been created yet")
        return cls._instance
