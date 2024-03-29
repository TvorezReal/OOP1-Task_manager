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

    def add_task(self):
        if not self.completed:
            self.tasks = []
            self.tasks.append(self)
        self.tasks.append(self)

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
mgr = Task("постричь газон", "2023-04-20")
mgr.add_task()
mgr2 = Task("нарисовать картину", "2023-05-30")
mgr2.add_task()
mgr.display_current_tasks()
print(tasks)
# mgr.mark_task_completed("нарисовать картину")
# mgr.display_current_tasks()
# mgr.mark_task_completed("постричь газон")
# mgr.display_current_tasks()