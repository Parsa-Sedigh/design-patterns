1. Component (Abstract Base Class): This is the foundation of the pattern, defining a common interface for all objects
   in the composition.
2. Leaf: A concrete class representing the simplest building blocks—objects that can’t have children.
3. Composite: Another concrete class that can contain other Component objects (leaves or other composites) and manages
   them.

### client code

Takes any Component (leaf or composite) and prints the result of its operation(). Because it uses the base `Component`
interface, it works **polymorphically, meaning no need to know the concrete type.**

### Summary

The beauty of this code lies in its adherence to the Composite pattern’s principles:

- Uniform Interface: Both Leaf and Composite inherit from Component, so client code can call operation() on any
  component without caring if it’s a leaf or a composite.
- Hierarchy Management: Composites handle child components, enabling complex tree structures.
- Polymorphism: The client functions (client_code and client_code2) operate on the abstract Component type, making the
  code flexible and reusable.
- Recursive Composition: The Composite’s operation() method recursively processes its children, building the result
  bottom-up.

This pattern is perfect for scenarios like file systems (files and folders), UI components (buttons and panels), or
organizational charts—anytime you need to treat single items and groups uniformly.