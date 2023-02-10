import random
import string
import pandas as pd
from time import time
import sys


names = ['Данил','Иван', 'Богдан', 'Петр', 'Владимир', 'Алекснадр', 'Кирилл', 'Максим', 'Артем', 'Леонид', 'Даниил', 'Виктор', 'Антон', 'Андрей', 'Амир', 'Алексей', 'Данила', 'Захар', 'Роман', 'Тимофей', 'Эрик', 'Лука', 'Вячеслав', 'Серафим', 'Валентин', 'Павел', 'Илья', 'Олег', 'Герман', 'Филлип', 'Макар', 'Яков', 'Родион', 'Карим', 'Марат', 'Егор', 'Борис', 'Валерий', 'Марк', 'Вадим', 'Руслан', 'Сергей', 'Мирон', 'Адам', 'Арсений', 'Платон', 'Святогор', 'Игнат', 'Марсель', 'Ростислав', 'Тигран', 'Ян', 'Всеволод', 'Никита', 'Святогор', 'Ярослав', 'Ринат']
surnames = ['Штокман', 'Друх', 'Белый', 'Сидоров', 'Петров', 'Гаркин', 'Иванов', 'Ульянов', 'Гайдар', 'Зыкин', 'Долгопрудов', 'Одинцов', 'Фомин', 'Чухно', 'Перцовский', 'Засулич', 'Стариков', 'Былов', 'Зеркалин', 'Ландер', 'Ананьев', 'Копырин', 'Бестужев', 'Антохин', 'Ваганов', 'Белопухов', 'Плетнев', 'Душин', 'Быстров', 'Бодров', 'Волков', 'Колесник', 'Онищенко', 'Силин', 'Дмитриев', 'Агарков', 'Гоголев', 'Литовка', 'Мазур', 'Кондратьев', 'Семиклит', 'Ластувка', 'Сазанов', 'Бордуков', 'Мкртчян', 'Агасян', 'Вершков', 'Фролов', 'Гилинский', 'Бичурин', 'Смирнов', 'Кириленко', 'Япаров', 'Кольба', 'Демешко', 'Мисюрин', 'Филатов', 'Третьяков', 'Ахматов', 'Мелихов', 'Шацкий', 'Сиверс', 'Бычков', 'Апьюк', 'Кущ', 'Солженицын', 'Починок', 'Новосильцев', 'Хатит', 'Вислогубов', 'Пиронко', 'Клюев', 'Франич', 'Крупеев', 'Карнадолин', 'Образцов', 'Савин', 'Еремеев', 'Ведерников', 'Овдиенко', 'Тихонов', 'Соловьев', 'Писарев', 'Филиппов', 'Куля', 'Капшук', 'Петрик', 'Тур', 'Голик', 'Парамонов', 'Федотов', 'Карпика', 'Мицик']
patronymic = ['Данилович', 'Иванович', 'Богданович', 'Петрович', 'Владимирович', 'Максимович', 'Леонидович', 'Александрович', 'Даниилович', 'Антонович', 'Андреевич', 'Алексеевич',  'Тимофеевич', 'Вячеславович', 'Серафимович', 'Валентинович', 'Павлович', 'Игоревич', 'Олегович', 'Германович', 'Муратович', 'Макарович', 'Артурович', 'Каримович', 'Егорович', 'Валерьевич', 'Русланович', 'Сергеевич', 'Миронович', 'Платонович', 'Игнатович', 'Янович', 'Григорьевич', 'Матвеевич', 'Родомирович', 'Федорович', 'Иосипович', 'Ильич', 'Захарьевич', 'Ефимович']
rank = ['матрос', 'старший матрос', 'младший сержант', 'сержант', 'рядовой', 'прапорщик', 'старший прапорщик','младший лейтенант', 'лейтенант', 'капитан', 'майор', 'полковник', 'подколковник', 'генерал-майор', 'мичман', 'старший мичман', 'генерал армии', 'генерал-полковник']

def make_table(n):
    full_names = []
    ranks = []
    numbers = []
    ages = []
    for i in range(n):
        name = ''.join(random.sample(surnames,1)) + ' ' + ''.join(random.sample(names,1)) + ' ' + ''.join(random.sample(patronymic ,1))
        full_names.append(name)
        ranks.append(''.join(random.sample(rank,1)))
        numbers.append(random.randint(1, 20))
        ages.append(random.randint(20, 65))
    table_name = 'table' + str(n) + '.xlsx'
    df = pd.DataFrame({'ФИО': full_names, 'звание': ranks, 'номер роты': numbers, 'возраст': ages})
    df.to_excel(table_name, index= False)
    print(table_name)

def read_table(n):
    tables = []
    for i in n:
        table_name = 'table' + str(i) + '.xlsx'
        table_from = pd.read_excel(table_name)
        tables.append(table_from)
    return tables

class Table:
    def __init__(self, raw: pd.core.series.Series):
        self.name = raw[0]
        self.status = raw[1]
        self.number = raw[2]
        self.age = raw[3]

    def __eq__(self, other):  # x = y
        if self.name == other.name:
            if self.status == other.status:
                if self.number == other.number:
                    if self.age == other.age:
                        return True
        return False

    def __ne__(self, other):  # x != y
        if self == other:
            return False
        else:
            return True

    def __lt__(self, other):  # x < y
        if self.status < other.status:
            return True
        elif self.status == other.status:
            if self.name < other.name:
                return True
            elif self.name == other.name:
                if self.number < other.number:
                    return True
        return False

    def __gt__(self, other):  # x > y
        if self.status > other.status:
            return True
        elif self.status == other.status:
            if self.name > other.name:
                return True
            elif self.name == other.name:
                if self.number > other.number:
                    return True
        return False

    def __le__(self, other):  # x <= y
        if (self < other) or (self == other):
            return True
        else:
            return False

    def __ge__(self, other):  # x >= y
        if (self > other) or (self == other):
            return True
        else:
            return False

def table_to_class(pds):
    objects = []
    for pd in pds:
        x = []
        for i in range(len(pd)):
            ob = Table(pd.iloc[i])
            x.append(ob)
        objects.append(x)
    return objects

def class_to_table(obj):
    sorted_names = []
    sorted_numbers = []
    sorted_statuses = []
    sorted_ages = []
    for i in obj:
        sorted_names.append(i.name)
        sorted_numbers.append(i.number)
        sorted_statuses.append(i.status)
        sorted_ages.append(i.age)
    sorted_df = pd.DataFrame({'ФИО': sorted_names, 'звание': sorted_statuses, 'номер роты': sorted_numbers, 'возраст': sorted_ages})
    return sorted_df

def select_sort(x):
    start = time()
    for i in range(len(x) - 1):
        mini = i # меняем номер первого рассматриваемого элемента
        for j in range(i + 1, len(x)): # сравниваем его со всеми "следующими элементами"
            if x[j] < x[mini]: # ищем локальный минимум
                mini = j
        x[i], x[mini] = x[mini], x[i] # найденный локальный минимум меняем местами с первым рассматриваемым элементов
    end = time()
    period = end - start
    return x, period

def insert_sort(x):
    start = time()
    for i in range(1, len(x)): # начинаем с 1, потому что первый элемент = первый отмортированный подмассив
        element = x[i]
        j = i-1
        # сравнимаем i-ый элемент с предыдущими (которые хранятся в уже отсортированной части списка)
        while j >=0 and element < x[j] : # если сравнимаемый элмент меньше предыдущего
            x[j+1] = x[j] # сдвигаем элемент, меньше которого он оказался
            j -= 1 # меняем счетчик, чтобы сравнимать со "следующими" (предыдущими) эл-тами уже отсортированной части списка
        x[j+1] = element # помещаем сравнимаемый элемент на нужное место
    end = time()
    period = end - start
    return x, period

sys.setrecursionlimit(1000000)
def change_pose(x, i, n):  # сравнимает iый элемент с его дочерними
    # n - первые n элементов, которые нужны учитывать
    i_left = 2 * i + 1  # левый дочерний узел
    i_right = 2 * i + 2  # правый дочерний узел
    i_maxi = i
    if i_left <= n and x[i_left] > x[i_maxi]:  # !! <=n - входит в нужный нам диапазон
        i_maxi = i_left
    if i_right <= n and x[i_right] > x[i_maxi]:  # !! <=n - входит в первые n  элементов списка
        i_maxi = i_right

    if i_maxi == i:  # поменялось ли значение
        return
    else:
        x[i_maxi], x[i] = x[i], x[i_maxi]  # меняем с одним из дочерних (макс) узлов
        change_pose(x, i_maxi, n)  # продолжаем процедуру для нового положения узла - для ноого списка


def make_tree(x):
    middle = len(x) // 2
    for i in reversed(range(0, middle + 1)):
        change_pose(x, i, len(x) - 1)


def pyramid_sort(x):
    start = time()
    make_tree(x)  # строим пирамиду / дерево
    for i in reversed(range(0, len(x))):  # идем с конца в начало
        x[0], x[i] = x[i], x[0]
        change_pose(x, 0, i - 1)
    end = time()
    period = end - start
    return x, period








