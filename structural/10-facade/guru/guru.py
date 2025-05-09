class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

    def get_ready1(self):
        return "Subsystem1: Ready!"

    # complex stuff going on ...

    def operation_n(self):
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def get_ready2(self):
        return "Subsystem2: Ready!"

    # complex stuff going on ...

    def operation_z(self):
        return "Subsystem2: Fire!"


class Facade:
    """
    The Facade class provides simple access point to the complex logic of one or
    several subsystems.

    The Facade delegates the client requests to the appropriate objects within the subsystem.

    The Facade is also responsible for managing subsystems lifecycle. All of this shields the
    client from the undesired complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2):
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """

        results = []

        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.get_ready1())
        results.append(self._subsystem2.get_ready2())

        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())

        return "\n".join(results)


def client_code(facade: Facade):
    """
    The client code works with complex subsystems through a simple access point
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    #
    # Anyway, facade can create the subsystems if they're not provided to it.

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)

    client_code(facade)

# Facade initializes subsystems:
# Subsystem1: Ready!
# Subsystem2: Get ready!
# Facade orders subsystems to perform the action:
# Subsystem1: Go!
# Subsystem2: Fire!
