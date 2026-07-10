from engine.serialization.serializable import Serializable

class Component(Serializable):
    """
    Base component class.

    Handles the registry of classes
    """

    registry = {}

    
    def __init_subclass__(cls):
        super().__init_subclass__()

        # Do not register abstract base class
        if cls is not Component:
            Component.registry[cls.__name__] = cls