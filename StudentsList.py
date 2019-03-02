import json
import os

clear = lambda: os.system('cls')

class Student:

    changed = False # Проверка на внесенные изменения

    # Словарь сообщений
    messages = {'exit': "Нажмите любую клавишу для выхода...",
    'filenotfound': "Ошибка! Файл students.json не найден!\n",
    'jsondecode_error': "Ошибка! Невозможно обработать файл students.json\n",
    'unknownerror': "Неизвестная ошибка\n",
    'blankfile': "Файл students.json пуст!",
    'commandslist': "[1 - Список студентов] \n[2 - Добавить студента] \n[3 - Удалить студента] \n[4 - Выход]",
    'studentadding': "\n/Добавление студента/\n",
    'newstudentname': "\nИмя нового студента: ",
    'newstudentsurname': "\nФамилия нового студента: ",
    'studentremoving': "\n/Удаление студента/\n",
    'deletestudentname': "\nИмя удаляемого студента: ",
    'deletestudentsurname': "\nФамилия удаляемого студента: ",
    'leaving': "\n/Выход/\n",
    'savechanges': "Сохранить изменения? [Y/N] > ",
    'unknownvalue': "Неизвестное значение!",
    'unknowncommand': "Неизвестная команда!",
    'command': "\n>>> "}

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

        except FileNotFoundError: # Файл не найден
            print(self.messages['filenotfound'])
            input(self.messages['exit'])
            exit()
        except json.JSONDecodeError: # Ошибка десериализации
            print(self.messages['jsondecode_error'])
            input(self.messages['exit'])
            exit()
        except:
            print('unknownerror') # Неизвестная ошибка
            input(self.messages['exit'])
            exit()

    def viewStudentList(self):
        # Если в studentsJSON что то есть
        if self.studentslist:
            i = 1
            clear()
            for student in self.studentslist: # Перебрать список и вывести каждого студента в новой строке
                print(str(i) + "]" + " " + student)
                i += 1
            print("\nКоличество студентов: " + str(len(self.studentslist))) # Вывод количества студентов
        else:
            clear()
            print(self.messages['blankfile'])
        # Иначе - вывод сообщение о пустом файле
    def addStudent(self, studentName = None, studentSurname = None):
        # Обьединение имени и фамилии студента в одну переменную
        student = studentName + " " + studentSurname

        if not student in self.studentslist:
            # Добавление нового элемента в конец списка
            self.studentslist.append(student)
            clear()
            print("Студент " + student + " успешно добавлен в базу!")
            self.changed = True # Внесены изменения
        else:
            clear()
            print("Студент " + student + " уже есть в базе!")

    def deleteStudent(self, studentName = None, studentSurname = None):
        # Обьединяем имя и фамилию студента
        student = studentName + " " + studentSurname

        # Если студент найден в базе
        if student in self.studentslist:
            clear()
            self.studentslist.remove(student) # Удаление студента из базы
            print("Студент " + student + " успешно удален из базы!")
            self.changed = True # Внесены изменения
        else: # Если такого студента не существует...
            clear()
            print("Студент " + student + " не найден в базе")
        
    def exit(self, save = True):
        if save: # Если передана команда сохранить изменения
            open('students.json' , 'w').write(json.dumps(self.studentslist)) # ...сериализовать изменения в student.json файл
        exit()

if __name__ == "__main__":
    student = Student() # Создание экземпляра класса Student
    while True:
        print("\n" * 4, "#" * 20, sep="") # Разделитель
        print(student.messages['commandslist']) # Список команд

        command = input(student.messages['command'])
        if command == '1': # Показ списка студентов
            clear()
            student.viewStudentList()
        elif command == '2': # Добавление студента
            clear()
            student.viewStudentList()
            print("\n", "#" * 20, sep="") # Разделитель
            print(student.messages['studentadding'])
            studentName = input(student.messages['newstudentname']) # Имя нового студента
            clear()
            student.viewStudentList()
            print("\nИмя: " + studentName)
            studentSurname = input(student.messages['newstudentsurname']) # Фамилия нового студента
            student.addStudent(studentName, studentSurname) # Добавление студента в базу
        elif command == '3': # Удаление студента
            clear()
            student.viewStudentList()
            print("\n", "#" * 20, sep="") # Разделитель
            print(student.messages['studentremoving'])
            studentName = input(student.messages['deletestudentname']) # Имя удаляемого студента
            clear()
            student.viewStudentList()
            print("\nИмя: " + studentName)
            studentSurname = input(student.messages['deletestudentsurname']) # Фамилия удаляемого студента
            student.deleteStudent(studentName, studentSurname) # Удаление студента из базы
        elif command == '4': # Выход
            clear()
            print(student.messages['leaving'])
            if student.changed: # Если внесены изменения - вывести предложение о сохранении изменений в файл
                command = input(student.messages['savechanges'])
                if command == 'Y' or command == 'y': student.exit()
                elif command == 'N' or command == 'n': student.exit(False)
                else:
                    clear()
                    print(student.messages['unknownvalue'])
                    input(student.messages['exit'])
                    clear()
            elif not student.changed: # Если изменения не внесены - выйти из программы
                clear()
                input(student.messages['exit'])
                student.exit(False)
        else: # Неизвестная команда
            print(student.messages['unknowncommand'])