from abc import ABC, abstractmethod
from enum import Enum

# Pros of this pattern:
# 1. If we don't use this pattern, we could have complex object creations using new() and it could be that one object requires
# other objects to pass to it. So it can get pretty complex.
# 2. we could have


class Burger(ABC):
    def __init__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Burgers(Enum):
    CHEESE = "CHEESE"
    DELUXECHEESE = "DELUXECHEESE"
    VEGAN = "VEGAN"
    DELUXEVEGAN = "DELUXEVEGAN"


class CheeseBurger(Burger):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class DeluxeCheeseBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Deluxe Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class VeganBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Vegan Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class DeluxeVeganBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "DeluxeVegan Burger"
        # set other attributes...

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class BurgerStore(ABC):

    @abstractmethod
    def create_burger(self, item: Burgers) -> Burger:
        pass

    def order_burger(self, type: Burgers) -> Burger:
        burger = self.create_burger(type)
        print(f"--- Making a {burger.get_name()} ---")
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger


class CheeseBurgerStore(ABC):
    @abstractmethod
    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.CHEESE:
            return CheeseBurger()

        if item == Burgers.DELUXECHEESE:
            return DeluxeCheeseBurger()


class VeganBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.VEGAN:
            return VeganBurger()
        elif item == Burgers.DELUXEVEGAN:
            return DeluxeVeganBurger()
        else:
            return None