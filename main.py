
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


class Store():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = dict()

    def add_item(self, item, price):
        self.items[item] = price

    def del_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Ошибка при удалении товара сейчас в магазине {self.name} нет товара {item}")

    def get_price_item(self, item):
        if item in self.items:
            return self.items[item]
        else:
            return None


    def new_price_item(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
        else:
            print(f"Ошибка при назначении новой цены  товарв сейчас в магазине {self.name} нет товара {item}")




def print_task(l1):    # l1 содержит список Задач
                        # функция выводит список невыполненных задач
    for el in l1:
        if not el.status:
            res = f'задача {el.desc} еще не выполнена'
            print(res)



print("Привет")

mag = Store("Дикси", "Москва")
print(mag.items)
mag.add_item("яблоки", 100)
mag.add_item("бананы", 140)
mag.add_item("груша", 240)
mag.add_item("клубника", 340)
print("печать 1")
print(mag.items)
mag.del_item("груша")
mag.del_item("груша")
print("печать 2")
print(mag.items)
print(f" цена банан =  {mag.get_price_item('бананы') }")
print(f" цена арбуза =  {mag.get_price_item('арбуз') }")

mag.new_price_item("бананы", 150)
print(f" новая цена банан =  {mag.get_price_item('бананы') }")
