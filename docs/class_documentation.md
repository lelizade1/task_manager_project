WorkItem:
An abstract base class that holds the common attributes such as id, title and
status. The ID can be provided manually or auto-generated using uuid. It requires
child classes to implement the get_details method.

Task:
Child of WorkItem. In addition to the basic fields, it has a priority field which
can be High, Medium or Low. It provides its own version of get_details.

SubTask:
Also a child of WorkItem. It holds a parent task ID which connects it to a main
task. Has its own get_details method to show the relationship.

TeamMember:
Simple class to store name and role of a team member. Currently not used much
but can be extended later.

WorkItemFactory:
A small helper that creates either a Task or SubTask based on a string input.
This keeps object creation organized.

TaskRepository:
Handles reading and writing data to the JSON file. It also checks if an ID
already exists which helps prevent duplicates. It returns raw lists of dicts
from the file for displaying.

TaskService:
The main operational layer. It contains methods like `create_task`, `create_subtask`,
`get_tasks`, `update_task_status`, and `delete_task`. It validates business rules
(non-empty titles, correct priority values) before calling the repository.

SortStrategy (and subclasses):
Abstract base class for sorting. `SortByTitle` sorts tasks alphabetically.
`SortByPriority` sorts them by High -> Medium -> Low.

Logger:
A utility set up in `utils/logger.py`. It writes info and error messages to `app.log`
and prints them to the console, aiding in debugging and tracking system usage.

main.py:
The user interface of the project. It shows menu options, accepts input, and calls
TaskService methods to perform actions.
