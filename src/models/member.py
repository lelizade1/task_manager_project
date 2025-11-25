class TeamMember:
    def __init__(self, name, role="Member"):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"