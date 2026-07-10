class BaseSystem:
    """
    Base system class which all system classes inherits from

    Enforces the start and update method
    """

    def start(self):
        pass

    def update(self, dt):
        pass