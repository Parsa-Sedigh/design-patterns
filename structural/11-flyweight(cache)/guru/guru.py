import json
from typing import Dict, List


class Flyweight:
    """
    The Flyweight stores a common portion of the state (also called intrinsic
    state) that belongs to multiple real business entities. The Flyweight
    accepts the rest of the state (extrinsic state, unique for each entity) via
    its method parameters.

    In this example, each Flyweight obj contains a list of strs which displays
    a list of shared states among some objs in our program.
    """

    def __init__(self, shared_state: List[str]):
        self._shared_state = shared_state

    def operation(self, unique_state: List[str]):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)

        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet.
    """

    _flyweights: Dict[str, Flyweight] = {}  # shared_state -> Flyweight

    def __init__(self, initial_flyweights: List[List[str]]):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: List[str]) -> str:
        """
        Returns a Flyweight's string hash for a given state.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: List[str]):
        """
        Returns an existing Flyweight with a given state or creates a new one.

        Yeah, it's based on the state not the key because we can get a flyweight based
        on it's state since the states are constant between same objs.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.", shared_state)
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(factory: FlyweightFactory, plates: str, owner: str,
                               brand: str, model: str, color: str):
    print("\n\nClient: Adding a car to database.")

    # brand, model and color are shared among a lot of police cars, so they compose the `shared state` or intrinsic state.
    flyweight = factory.get_flyweight([brand, model, color])

    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    # NOTE: plates and owner are extrinsic state, so we pass it to flyweight methods.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()

# FlyweightFactory: I have 5 flyweights:
# Camaro2018_Chevrolet_pink
# C300_Mercedes Benz_black
# C500_Mercedes Benz_red
# BMW_M5_red
# BMW_X6_white
#
# Client: Adding a car to database.
# FlyweightFactory: Reusing existing flyweight.
# Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["CL234IR", "James Doe"]) state.
#
# Client: Adding a car to database.
# FlyweightFactory: Can't find a flyweight, creating new one.
# Flyweight: Displaying shared (["BMW", "X1", "red"]) and unique (["CL234IR", "James Doe"]) state.
#
# FlyweightFactory: I have 6 flyweights:
# Camaro2018_Chevrolet_pink
# C300_Mercedes Benz_black
# C500_Mercedes Benz_red
# BMW_M5_red
# BMW_X6_white
# BMW_X1_red
