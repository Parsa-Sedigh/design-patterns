from abc import ABC, abstractmethod


# Interface
class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_step_a(self) -> None:
        pass

    @abstractmethod
    def produce_step_b(self) -> None:
        pass

    @abstractmethod
    def produce_step_c(self) -> None:
        pass


class Product1:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self):
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """

        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results(we named it `product` method). That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language). So we define them in the concrete builder classes.

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """

        product = self._product
        self.reset()

        return product

    def produce_step_a(self) -> None:
        self._product.add('PartA1')

    def produce_step_b(self) -> None:
        self._product.add('PartB1')

    def produce_step_c(self) -> None:
        self._product.add('PartC1')


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.

    Instead of passing the Builder to the constructor of Director, we set the builder using
    a set method of Director. So that we don't have to instantiate a director per builder.
    We just need one director.

    This way, we can use a different builder each time we produce something with the director.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """

        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self):
        self.builder.produce_step_a()

    def build_full_featured_product(self):
        self.builder.produce_step_a()
        self.builder.produce_step_b()
        self.builder.produce_step_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    builder = ConcreteBuilder1()

    director = Director()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    
    builder.product.list_parts()  # builder gets freshened at this point

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    builder.produce_step_a()
    builder.produce_step_b()

    # reset() is called when we access the product field. So after the next line, builder is freshened and ready to
    # build another product
    builder.product.list_parts()

############# Execution result #############

# Standard basic product:
# Product parts: PartA1
#
# Standard full featured product:
# Product parts: PartA1, PartB1, PartC1
#
# Custom product:
# Product parts: PartA1, PartB1
