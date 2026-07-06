import os

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


class Task:
    def __init__(self, id, title, description, isdone=False):
        self.id = id
        self.title = title
        self.description = description
        self.isdone = isdone

    def __str__(self):
        status = "x" if self.isdone else " "
        return f"[{status}] ID: {self.id} | {self.title}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_id = len(self.tasks) + 1
        new_task = Task(new_id, title, description)
        self.tasks.append(new_task)

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        raise ValueError("Задача не найдена")

    def mark_as_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.isdone = True
                return True
        raise ValueError("Задача не найдена")

    def show_tasks(self):
        if not self.tasks:
            print(f"{RED}Список задач пуст!{RESET}")
            return

        for task in self.tasks:
            print(task)


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        os.system("clear")
        print("\n--- Менеджер задач ---")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Пометить задачу как выполненную")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\n--- Твои задачи ---")
            manager.show_tasks()
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "2":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")

            manager.add_task(title, description)
            print(f"{GREEN}Задача успешно добавлена!{RESET}")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "3":
            print("\n--- Удаление задачи ---")
            manager.show_tasks()

            if manager.tasks:
                try:
                    task_id = int(input("\nВыбери ID задачи для удаления: "))
                    manager.remove_task(task_id)
                    print(f"{GREEN}Задача успешно удалена!{RESET}")
                except ValueError:
                    print(f"{RED}Ошибка: Неверный ID или введены не цифры!{RESET}")

            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "4":
            print("\n--- Выполнение задачи ---")
            manager.show_tasks()

            if manager.tasks:
                try:
                    task_id = int(input("\nВыбери ID задачи для отметки: "))
                    manager.mark_as_done(task_id)
                    print(f"{GREEN}Статус задачи успешно обновлен!{RESET}")
                except ValueError:
                    print(f"{RED}Ошибка: Неверный ID или введены не цифры!{RESET}")

            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "5":
            print("Пока-пока!")
            break

        else:
            print(f"{RED}Неверный ввод...{RESET}")
            input("\nНажми Enter, чтобы продолжить...")
