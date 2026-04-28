from user import User
from task import Task,get_incomplete_tasks

Hasan = User("Hasan", "Hasan22issa@gmail.com")

t1 = Task("Write tests", "Cover the core modules")
t2 = Task("Update docs", "Revise the README")
t3 = Task("Fix bug #42", "Null pointer in parser")
list1 = [t1,t2,t3]
t1.assign(Hasan)
t2.assign(Hasan)
t3.assign(Hasan)

t2.complete()  # only this one is done

incomplete = get_incomplete_tasks(list1)
for task in incomplete:
    task.display()
    print()