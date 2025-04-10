# interface
# or Publisher
from __future__ import annotations

from abc import abstractmethod, ABC
from random import randrange
from typing import List


# interface
class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @property
    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def attach(self, observer: Observer):
        """
        Attach an observer to the subject.
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """
        Detach an observer from the subject.
        """

        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """

        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """
    _state: int = None

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    _observers: List[Observer] = []

    @property
    def state(self):
        return self._state

    def attach(self, observer: Observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    """
    The subscription management methods:
    """

    def notify(self):
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    Subject can pass whatever it thinks is ok(including subject obj itself).
    """

    @abstractmethod
    def update(self, subject: Subject):
        """
        Receive update from subject.
        """

        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

# Subject: Attached an observer.
# Subject: Attached an observer.
#
# Subject: I'm doing something important.
# Subject: My state has just changed to: 0
# Subject: Notifying observers...
# ConcreteObserverA: Reacted to the event
# ConcreteObserverB: Reacted to the event
#
# Subject: I'm doing something important.
# Subject: My state has just changed to: 5
# Subject: Notifying observers...
# ConcreteObserverB: Reacted to the event
#
# Subject: I'm doing something important.
# Subject: My state has just changed to: 0
# Subject: Notifying observers...
# ConcreteObserverB: Reacted to the event
