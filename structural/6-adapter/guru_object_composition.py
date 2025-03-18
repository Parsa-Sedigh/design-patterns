class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    So it's already being used by the client.
    Now the client wants to use the Adaptee class, but it's incompatible, because the client code can only call a method named
    request() not specific_request().
    """

    def request(self) -> str:
        return "Target: The default target's behavior."

 
class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.

    Adapter INHERITS the class that the client is already working with(Target class). But it receives the incompatible class
    through it's constructor. So that it can make it compatible with the inherited class.
    """

    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    But it can't work with Adaptee class since it doesn't have the request() method.
    So we can use use the Adapter class.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)

# Client: I can work just fine with the Target objects:
# Target: The default target's behavior.
#
# Client: The Adaptee class has a weird interface. See, I don't understand it:
# Adaptee: .eetpadA eht fo roivaheb laicepS
#
# Client: But I can work with it via the Adapter:
# Adapter: (TRANSLATED) Special behavior of the Adaptee.
