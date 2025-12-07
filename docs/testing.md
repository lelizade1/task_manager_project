Testing mainly focuses on checking the repository and factory behavior.

For the repository:
- Save a task and see if it appears in the returned list.
- Check whether task_exists returns true when an item with that ID is saved.
- Confirm it returns false for IDs that don’t exist.

For the factory:
- Ensure that asking for a “task” creates a Task object.
- Asking for a “subtask” creates a SubTask.
- Check that automatic ID generation creates an 8-character ID.

The tests use temporary files so they don’t affect the real tasks.json.
