from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


# interface
class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state(which are stored inside memento's private fields).
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class Originator:
    """
    The Originator:
    1. holds some important state that may change over time.
    2. a method for saving the state inside a memento
    3. a method for restoring the state from it.
    """

    """
    For the sake of simplicity, the originator's state is stored inside a single
    variable.
    """
    _state = None

    def __init__(self, state: str):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_sth(self):
        """
        The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Returns the current state inside a memento.
        The stack of mementos are stored inside Caretaker class.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        """
        Restores the Originator's state from a memento object.
        """

        # get_state is not inside the Memento interface, because the memento's state
        # should be hidden from the outside and is only visible to Originator.
        if isinstance(memento, ConcreteMemento):
            self._state = memento.get_state()
            print(f"Originator: My state has changed to: {self._state}")
        else:
            raise TypeError("Invalid memento type")


# impls Memento interface
class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        The Originator uses this method when restoring its state.
        """

        return self._state

    """
    The rest of the methods are used by the Caretaker to display metadata:
    """

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator):
        self._mementos = []
        self.originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self.originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")

        try:
            self.originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")

        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_sth()

    caretaker.backup()
    originator.do_sth()

    caretaker.backup()
    originator.do_sth()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

# Originator: My initial state is: Super-duper-super-puper-super.
#
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat
#
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
#
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: cvIYsRilNOtwynaKdEZpDCQkFAXVMf
#
# Caretaker: Here's the list of mementos:
# 2019-01-26 21:11:24 / (Super-dup...)
# 2019-01-26 21:11:24 / (wQAehHYOq...)
# 2019-01-26 21:11:24 / (lHxNORKcs...)
#
# Client: Now, let's rollback!
#
# Caretaker: Restoring state to: 2019-01-26 21:11:24 / (lHxNORKcs...)
# Originator: My state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
#
# Client: Once more!
#
# Caretaker: Restoring state to: 2019-01-26 21:11:24 / (wQAehHYOq...)
# Originator: My state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat
