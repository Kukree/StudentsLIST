import json
import os

clear = lambda: os.system('cls')

class Student:
    def __init__(self):
        try:
            # Если в studentsJSON что то есть
            # Десерилизовать данные в нем в обычный список
            studentslist = open("students.json").read()
            if studentslist:
                self.studentslist = json.loads(studentslist)
            else:
                self.studentslist = []
            # Иначе - создать новый список

        except FileNotFoundError:
            print("Ошибка! Для начала создайте файл students.json")
            input("Нажмите любую клавишу для выхода...")
            exit()
        except json.JSONDecodeError:
            print("Ошибка! Невозможно обработать файл students.json")
            input("Нажмите любую клавишу для выхода...")
            exit()
        except:
            print("Неизвестная ошибка")
            input("Нажмите любую клавишу для выхода...")
            exit()

    def viewStudentList(self):
        # Если в studentsJSON что то есть
        if self.studentslist:
            i = 1
            clear()
            for student in self.studentslist:
                print(str(i) + " " + student)
                i += 1
            print("\nКоличество студентов: " + str(len(self.studentslist)))
        else:
            clear()
            print("students.json пуст!")
        # Иначе - вывод сообщения
    def addStudent(self, studentName = None, studentSurname = None):
        if not studentName:
            if len(studentName) < 3:
                print("\nИмя студента короче трех символов или пустое")
            # Если длина имени студента короче трех символов - вывод ошибки
            
        if not studentSurname:
            studentSurname = input("Фамилия нового студента: ")
            if len(studentSurname) < 3:
                print("\nФамилия студента короче трех символов или пустое")
            # Если длина фамилии студента короче трех символов - вывод ошибки

        # Обьединение имени и фамилии студента в одну переменную
        student = studentName + " " + studentSurname

        if not student in self.studentslist:
            # Добавление нового элемента в конец списка
            self.studentslist.append(student)
            clear()
            print("Студент " + student + " успешно добавлен в базу!")
        else:
            clear()
            print("Студент " + student + " уже есть в базе!")

    def deleteStudent(self, studentName = None, studentSurname = None):
        if not studentName:
            if len(studentName) < 3:
                print("\nИмя студента короче трех символов или пустое")
            # Если длина имени студента короче трех символов - вывод ошибки
        if not studentSurname:
            studentSurname = input("Фамилия удаляемого студента: ")
            if len(studentSurname) < 3:
                print("\nФамилия студента короче трех символов или пустое")
            # Если длина фамилии студента короче трех символов - вывод ошибки

        # Обьединяем имя и фамилию студента
        student = studentName + " " + studentSurname

        # Если студент найден в базе
        if student in self.studentslist:
            clear()
            self.studentslist.remove(student)
            print("Студент " + student + " успешно удален из базы!")
        else:
            clear()
            print("Студент " + student + " не найден в базе")
        # Если такого студента не существует...
        
    def exit(self, save = True):
        if save:
            open('students.json' , 'w').write(json.dumps(self.studentslist))
        exit()

if __name__ == "__main__":
    student = Student()
    while True:
        print("\n" * 4, "#" * 20, sep="")
        print("[1 - Список студентов] \n[2 - Добавить студента] \n[3 - Удалить студента] \n[4 - Выход]")

        command = input("\n>>> ")
        if command == '1': # Показ списка студентов
            clear()
            student.viewStudentList()
        elif command == '2': # Добавление студента в базу
            print("\n/Добавление студента/\n")
            studentName = input("Имя нового студента: ")
            studentSurname = input("Фамилия нового студента: ")
            student.addStudent(studentName, studentSurname)
        elif command == '3': # Удаление студента из базы
            print("\n/Удаление студента/\n")
            studentName = input("Имя удаляемого студента: ")
            studentSurname = input("Фамилия удаляемого студента: ")
            student.deleteStudent(studentName, studentSurname)
        elif command == '4': # Выход
            print("\n/Выход/\n")
            command = input("Сохранить изменения? [Y/N] > ")
            if command == 'Y': student.exit()
            elif command == 'N': student.exit(False)
            else: print("Неизвестное значение")
        else:
            print("Неизвестная команда")