This project is a small Task Management System that works through the terminal.
The purpose is to let a user create tasks and subtasks, save them, and view them
later. The system is simple but tries to follow basic OOP ideas and design rules.

Tasks can have a priority and SubTasks must always belong to an existing task.
Each item is saved to a JSON file. IDs can be written by the user or automatically
generated. The program performs checks such as duplicate IDs and missing parent
IDs, so that the data stays consistent.

Overall the system is mainly for practicing OOP (inheritance, abstraction),
separating logic into different files, and using a small data layer.


Sprint 1 Goals
Establish a solid OOP architecture.
Implement core classes.
Apply SOLID, GRASP, and CUPID principles.
Implement Create/Read operations.
Add a Repository layer for JSON persistence.
Add unit testing.
Deliver initial documentation.
Produce a runnable prototype (via main.py).
The Sprint 1 implementation fully meets the requirements defined in the PDF.
