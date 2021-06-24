class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)

    def get_st(self):
        return self.__st

    def add_elem(self, elem):
        self.__st.append(elem)

    def extract(self, elem):
        if self.__st:
            return self.__st.pop()
        else:
            return None


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)} {self.task[i_priority]}\n')
            return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].add_elem(task)

    def done_task(self, task):
        for i_priority, i_task in self.task.items():
            if task in i_task.get_st():
                i_task.extract(task)
            if not i_task.get_st():
                del self.task[i_priority]
                break


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.done_task("отдохнуть")
print(manager)
