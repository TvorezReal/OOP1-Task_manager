class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append({"description": description, "due_date": due_date, "status": "incomplete"})

    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "complete"
                print(f"Задача {description} выполнена.")
            else:
                print(f"Задача {description} не найдена.")

    def display_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task["status"] == "incomplete":
                print(f"{task['description']} - {task['due_date']} ")


task_manager = Task()
task_manager.add_task("Выучить Python", "2023-05-30")
task_manager.add_task("Постричь газон", "2023-04-20")
task_manager.display_tasks()
task_manager.complete_task("Постричь газон")
task_manager.display_tasks()
