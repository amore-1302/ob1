
class Task():
    def __init__(self,desc, deadline, status=False):
        self.desc = desc
        self.deadline = deadline
        self.status = status

    def add_task(self,desc, deadline, status):
        self.desc = desc
        self.deadline = deadline
        self.status = status

    def executed(self):
        self.status = True


def print_task( l1):    # l1 содержит список Задач
                        # функция выводит список невыполненных задач
    for el in l1:
        if not el.status:
            res = f'задача {el.desc} еще не выполнена'
            print(res)


print("Привет")