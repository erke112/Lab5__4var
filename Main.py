# животное -> млекопитающее -> парнокопытное
class Animal(object):
    # конструктор
    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age

    def __del__(self):
        print(self.__name, "удалён из памяти")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, Age):
        if Age in range(0, 1000):
            self.__age = Age
        else:
            print("Недопустимый возраст")

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)


class Mammal(Animal):
    def __init__(self, name="", age=0, KolvoZubov=10):
        Animal.__init__(self, name, age)
        self.__kolvozubov = KolvoZubov

    def __del__(self):
        print(self.Name, "удалён из памяти")

    def display_info(self):
        Animal.display_info(self)
        print("Количество зубов:", self.__kolvozubov)

    def __str__(self):
        return Animal.__str__(self) + "\tКоличество зубов: {}".format(self.__kolvozubov)

    @property
    def KolvoZubov(self):
        return self.__kolvozubov

    @KolvoZubov.setter
    def KolvoZubov(self, kolvo):
        if kolvo in range(0, 1000):
            self.__kolvozubov = kolvo
        else:
            print("Да не бывает столько")


class Even_toed_ungulate(Mammal):
    def __init__(self, name="", age=0, KolvoZubov=10, KolvoNog=4):
        Mammal.__init__(self, name, age, KolvoZubov)
        self.__kolvonog = KolvoNog

    def __del__(self):
        print(self.Name, "удалён из памяти")

    def display_info(self):
        Mammal.display_info(self)
        print("Количество ног:", self.__kolvonog)

    def __str__(self):
        return Mammal.__str__(self) + "\tКоличество ног: {}".format(self.__kolvonog)

    @property
    def KolvoNog(self):
        return self.__kolvonog

    @KolvoNog.setter
    def KolvoNog(self, kolvo):
        if kolvo in range(0, 1000):
            self.__kolvonog = kolvo
        else:
            print("Да не бывает столько")

f = []
while True:
    print(
        "1) Добавление\n2) Редактирование")
    print("3) Удаление\n4) Отображение данных")
    print("5) Поиск")
    print("6) Выход из программы")
    menu = input()
    if menu == "1":
        print("Добавить  1 - Абстрактное животное, 2 - млекопитающее, 3 - паронокопытное")
        try:
            toadd = int(input())
        except: toadd=0
        if toadd == 1:
            try:
                name, age = map(str, input("Введите название, возраст через пробел: ").split())
                age = int(age)
                f.append(Animal(name, age))
            except:
                print("Ошибка")
        elif toadd == 2:
            try:
                name, age, zub = map(str, input("Введите название, возраст, количество зубов через пробел: ").split())
                age = int(age)
                zub = int(zub)
                f.append(Mammal(name, age, zub))
            except:
                print("Ошибка")
        elif toadd == 3:
            try:
                name, age, zub, nog = map(str,
                                          input("Введите название, возраст, количество зубов и ног через пробел: ").split())
                age = int(age)
                zub = int(zub)
                nog = int(nog)
                f.append(Even_toed_ungulate(name, age, zub, nog))
            except:
                print("Ошибка")
        else:
            print("Что-то не то выбрано")
    elif menu == '2':
        print("Кого редактировать: ", end="\n")
        for i in range(len(f)):
            if isinstance(f[i], Even_toed_ungulate):
                print(i + 1, ": парнокопытное ",f[i].__class__, f[i].Name, sep="")
            elif isinstance(f[i], Mammal):
                print(i + 1, ": млекопитающее ", f[i].Name, sep="")
            elif isinstance(f[i], Animal):
                print(i + 1, ": животное ", f[i].Name, sep="")
        try:
            toredact = int(input()) - 1
            print("Что меняем? ", end="")
            if isinstance(f[toredact], Even_toed_ungulate):
                print("1 - Название, 2 - возраст, 3 - кол-во зубов, 4 - кол-во ног")
                red = int(input())
                print("Вводите новое значение: ", end="")
                new = input()
                if red == 1:
                    f[toredact].Name = new
                elif red == 2:
                    f[toredact].Age = int(new)
                elif red == 3:
                    f[toredact].KolvoZubov = int(new)
                elif red == 4:
                    f[toredact].KolvoNog = int(new)
                else:
                    print("Что-то не то выбрано")
            elif isinstance(f[toredact], Mammal):
                print("1 - Название, 2 - возраст, 3 - кол-во зубов")
                red = int(input())
                print("Вводите новое значение: ", end="")
                new = input()
                if red == 1:
                    f[toredact].Name = new
                elif red == 2:
                    f[toredact].Age = int(new)
                elif red == 3:
                    f[toredact].KolvoZubov = int(new)
                else:
                    print("Что-то не то выбрано")
            elif isinstance(f[toredact], Animal):
                print("1 - Название, 2 - возраст")
                red = int(input())
                print("Вводите новое значение: ", end="")
                new = input()
                if red == 1:
                    f[toredact].Name = new
                elif red == 2:
                    f[toredact].Age = int(new)
                else:
                    print("Что-то не то выбрано")
        except:
            print("Ошибка")
    elif menu == '3':
        print("Кого удалить? : ", end="\n")
        for i in range(len(f)):
            print(i + 1, ": ", f[i].Name, sep="")
        try:
            todel = int(input())
            f.pop(todel - 1)
        except:
            print("Ошибка")
    elif menu == '4':
        print("Вот кто есть:")
        for i in range(len(f)):
            print(f[i], sep="")
        if len(f) == 0:
            print("Никого нет")
    elif menu == '5':
        print("По какому критерию ищем? : 1 - Название, 2 - возраст, 3 - кол-во зубов, 4 - кол-во ног : ", end='')
        try:
            tofind = int(input())
            if tofind == 1:
                name = input("Введите название  ")
                for i in f:
                    if i.Name == name:
                        print(i)
            if tofind == 2:
                age = int(input("Введите возраст  "))
                for i in f:
                    if i.Age == age:
                        print(i)
            if tofind == 3:
                zub = int(input("Введите кол-во зубов  "))
                for i in f:
                    if isinstance(i, Mammal) or isinstance(i, Even_toed_ungulate):
                        if i.KolvoZubov == zub:
                            print(i)
            if tofind == 4:
                nog = int(input("Введите кол-во ног  "))
                for i in f:
                    if isinstance(i, Even_toed_ungulate):
                        if i.KolvoNog == nog:
                            print(i)
        except:
            print("Ошибка")
    elif menu == '6':
        break
