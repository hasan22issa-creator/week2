from user import User
from task import Task,get_incomplete_tasks

Hasan = User("Hasan", "Hasan22issa@gmail.com")

t1 = Task("Prepare presentation", "Create slides for project demo")
t2 = Task("Team meeting", "Discuss weekly progress with the team")
t3 = Task("Code review", "Review pull requests on GitHub")
list1 = [t1,t2,t3]
t1.assign(Hasan)
t2.assign(Hasan)
t3.assign(Hasan)

t2.complete()  # only this one is done

incomplete = get_incomplete_tasks(list1)
for task in incomplete:
    task.display()
    print()