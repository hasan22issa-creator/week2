class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.tasks: list = []
 
    def assign_task(self, task) -> None:
        """Called internally when a task is assigned to this user."""
        if task not in self.tasks:
            self.tasks.append(task)
 
    def display(self) -> None:
        print(f"User : {self.name}")
        print(f"Email: {self.email}")
        if self.tasks:
            print(f"Tasks ({len(self.tasks)}):")
            for task in self.tasks:
                print(f"  • [{task.status}] {task.title}")
        else:
            print("Tasks: none")
 
    def __repr__(self) -> str:
        return f"User(name={self.name!r}, email={self.email!r})"