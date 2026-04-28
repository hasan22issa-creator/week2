from user import User
 
class Task:
    VALID_STATUSES = {"open", "in-progress", "done"}
 
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.status = "open"
        self.owner: User | None = None
 
    def assign(self, user: User) -> None:
        """Assign this task to a user and update the user's task list."""
        self.owner = user
        user.assign_task(self)
        if self.status == "open":
            self.status = "in-progress"
        print(f"Task '{self.title}' assigned to {user.name}.")
 
    def complete(self) -> None:
        """Mark the task as done."""
        if self.status == "done":
            print(f"Task '{self.title}' is already done.")
            return
        self.status = "done"
        print(f"Task '{self.title}' marked as done.")
 
    def display(self) -> None:
        owner_name = self.owner.name if self.owner else "Unassigned"
        print(f"Task       : {self.title}")
        print(f"Description: {self.description}")
        print(f"Status     : {self.status}")
        print(f"Owner      : {owner_name}")
 
    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, status={self.status!r})"
    
def get_incomplete_tasks(tasks: list["Task"]) -> list["Task"]:
    """Return tasks that are not yet done."""
    return [task for task in tasks if task.status != "done"]