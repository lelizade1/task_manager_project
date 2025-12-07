The project uses a few basic design patterns:

Factory Pattern:
WorkItemFactory chooses whether to build a Task or a SubTask. This keeps the
object creation logic separate from main.py and avoids repeating code.

Repository Pattern (simplified):
TaskRepository works as the data access layer. It hides the JSON read/write
operations so the rest of the code does not deal directly with the file system.

Separation of Concerns:
Even though not a “pattern”, the project clearly separates model classes, the
repository, and the user interface, which makes the code easier to extend.

Strategy Pattern:
Used for sorting tasks. The `SortStrategy` abstract class allows swapping between
different sorting algorithms (`SortByTitle`, `SortByPriority`) at runtime without
changing the code that uses them.

These patterns make the project structure cleaner and reduce duplication.
