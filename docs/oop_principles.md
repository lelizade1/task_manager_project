# OOP Principles in This Project

### Abstraction
There is an abstract class called WorkItem. It contains the shared attributes
(id, title, status) and a method that child classes must implement. Task and
SubTask both come from this class.

### Encapsulation
The ID of each item is private (`__id`) and can only be accessed with the
property method called `id`. This prevents unwanted modification.

### Inheritance
Task and SubTask both inherit from WorkItem. They reuse the common attributes
while adding their own fields (Task has priority, SubTask has parent_id).

### Polymorphism
The method `get_details()` is implemented differently in Task and SubTask.
Also, WorkItemFactory returns Task or SubTask depending on what is requested.

### Extra
TeamMember is a small independent class for possible future extension.
