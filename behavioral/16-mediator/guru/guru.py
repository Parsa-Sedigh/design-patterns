from abc import ABC, abstractmethod


# interface
class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    @abstractmethod
    def notify(self, sender: object, event: str):
        pass


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: Mediator):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components(mediator handles the communication).
They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
    def do_a(self):
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component1.mediator = self

        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()

# Client triggers operation A.
# Component 1 does A.
# Mediator reacts on A and triggers following operations:
# Component 2 does C.
#
#
# Client triggers operation D.
# Component 2 does D.
# Mediator reacts on D and triggers following operations:
# Component 1 does B.
# Component 2 does C.
