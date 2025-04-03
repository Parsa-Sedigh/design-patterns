from abc import ABC, abstractmethod


# interface
class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        pass


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class SimpleCommand(Command):
    """
    Some commands can execute simple operations on their own,
    so they don't need a receiver to delegate the job.
    """

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str):
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        """
        Commands can delegate the work to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")

        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command not the receiver. The command knows what to do with the request.
    It can handle the req itself or call the correct receiver.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands:
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))

    receiver = Receiver()

    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

    invoker.do_something_important()

# Invoker: Does anybody want something done before I begin?
# SimpleCommand: See, I can do simple things like printing (Say Hi!)
# Invoker: ...doing something really important...
# Invoker: Does anybody want something done after I finish?
# ComplexCommand: Complex stuff should be done by a receiver object
# Receiver: Working on (Send email.)
# Receiver: Also working on (Save report.)
