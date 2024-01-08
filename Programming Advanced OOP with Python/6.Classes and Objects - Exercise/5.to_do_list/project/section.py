from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task = [task for task in self.tasks if task_name == task.name]
        if not task:
            return f"Could not find task with the name {task_name}"
        task = task[0]
        task.completed = True
        return f"Completed task {task.name}"

    def clean_section(self):
        count = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        text = '\n'.join(task.details() for task in self.tasks)
        return f"Section {self.name}:\n{text}"
