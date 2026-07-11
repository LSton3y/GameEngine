from engine.serialization.serializable import Serializable
from engine.serialization.registry import Registry


class Component(Serializable):
    """
    Base component class.
    """

    
    def __init_subclass__(cls):
        super().__init_subclass__()

        # Do not register abstract base class
        if cls is not Component:
            Registry.register(cls)