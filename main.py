# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.description} со сроком {self.due_date} - {'Выполнена' if self.completed else 'Не выполнена'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                return
        print("Задача не найдена.")

    def display_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.completed:
                print(task)

# Пример использования
mgr = TaskManager()
mgr.add_task("нарисовать картину", "2023-05-30")
mgr.add_task("постричь газон", "2023-04-20")
mgr.display_current_tasks()
mgr.mark_task_completed("постричь газон")
mgr.display_current_tasks()