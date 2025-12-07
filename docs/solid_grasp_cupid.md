# SOLID, GRASP and CUPID Principles

### SOLID

**S – Single Responsibility**  
Each file/class has one job. Repository only handles saving and reading.
Factory only creates objects. Models only describe data.

**O – Open/Closed**  
If we want another WorkItem type, we can extend WorkItem and just update
the factory without changing other parts too much.

**L – Liskov Substitution**  
Task and SubTask can be used anywhere a WorkItem is expected.

**I – Interface Segregation**  
Classes only contain methods they actually need. No unnecessary functions.

**D – Dependency Inversion**  
main.py depends on TaskRepository (a higher-level abstraction), not on
file I/O code directly.

---

### GRASP

**Controller:**  
main.py controls the flow and coordinates tasks.

**Creator:**  
WorkItemFactory creates Task or SubTask objects.

**High Cohesion & Low Coupling:**  
Each part is small and focused. Models, logic and storage are all separated.

---

### CUPID

**Composable:**  
Models + factory + repo work together well.

**Understandable:**  
Code names and structure are simple to follow.

**Predictable:**  
Validation and ID handling work the same way every time.

**Idiomatic:**  
Uses Pythonic structures like properties, uuid, and simple modules.

**Domain-based:**  
Task, SubTask, Repository etc. directly match the problem domain.
