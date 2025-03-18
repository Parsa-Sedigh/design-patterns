In adapter:

Object composition:

1. inherit the class that client can already work with(target)
2. get the adaptee in constructor
3. in the overridden method of `target`, call the incompatible method of adaptee with transformed data

Inheritance:

1. inherit both Target and Adaptee
2. when client calls the method it knows(`request()`), call the adaptee's method with transformed data

Note: In this context, object composition means that the Adapter class contains an instance of the Adaptee class as a
member (attribute) rather than inheriting from it.

How Object Composition Works Here:

1. The Adapter class inherits from Target, ensuring it provides a request() method, which is what the client expects.
2. Instead of inheriting from Adaptee, the Adapter stores an instance of Adaptee as an attribute (self.adaptee).
3. The Adapter then **delegates** call of client, from adapter.request() to adaptee.specific_request(), transforming the
   output as needed.