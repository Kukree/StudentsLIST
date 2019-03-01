import json
import os

clear = lambda: os.system('cls')

class Student:

    changed = False

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
                print(str(i) + "]" + " " + student)
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
            self.changed = True
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
            self.changed = True
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
            clear()
            print("\n/Добавление студента/\n")
            student.viewStudentList()
            studentName = input("\nИмя нового студента: ")
            clear()
            student.viewStudentList()
            print("\nИмя: " + studentName)
            studentSurname = input("\nФамилия нового студента: ")
            student.addStudent(studentName, studentSurname)
        elif command == '3': # Удаление студента из базы
            clear()
            print("\n/Удаление студента/\n")
            student.viewStudentList()
            studentName = input("\nИмя удаляемого студента: ")
            clear()
            student.viewStudentList()
            print("\nИмя: " + studentName)
            studentSurname = input("\nФамилия удаляемого студента: ")
            student.deleteStudent(studentName, studentSurname)
        elif command == '4': # Выход
            clear()
            print("\n/Выход/\n")
            if student.changed:
                command = input("Сохранить изменения? [Y/N] > ")
                if command == 'Y': student.exit()
                elif command == 'N': student.exit(False)
                else: print("Неизвестное значение")
            elif not student.changed:
                clear()
                input("Нажмите любую клавишу для выхода...")
                student.exit(False)
        else:
            print("Неизвестная команда!")