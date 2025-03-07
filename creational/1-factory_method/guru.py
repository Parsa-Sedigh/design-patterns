from abc import ABC, abstractmethod


############# Abstract classes #############

# INTERFACE - since all methods are abstract and have no logic in them. There's not a single concrete method.
class Product(ABC):
    """
    The Product interface DECLARES(since it's an abstract class) the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


# ABSTRACT CLASS - since it has some concrete methods
class Creator(ABC):
    """
    The Creator class DECLARES(since it's an abstract class) the factory method which is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self) -> Product:
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """

        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


##########################

############# Sub classes #############


class ConcreteCreator1(Creator):
    """
    Note that the signature of the methods of this class still use the ABSTRACT product type not it's concrete impl,
    even though the concrete product is actually returned from the methods (because we instantiate it in the methods). This
    way the Creator can stay independent of concrete product classes.

    So the concrete creator class, doesn't return any concrete product classes(like ConcreteProduct1).
    It still returns abstract Product, although it's being instantiated in the methods.
    """

    def factory_method(self) -> Product:
        pass


class ConcreteCreator2(Creator):
    def factory_method(self):
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


##########################


def client_code(creator: Creator):
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface(in our case, Product abstract class), you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

############# Execution result #############

# App: Launched with the ConcreteCreator1.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}
#
# App: Launched with the ConcreteCreator2.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
