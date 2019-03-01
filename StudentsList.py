import json
import os

clear = lambda: os.system('cls')

class Student:
    def contentChecking(self):
        pass

    def fileChecking(self):
        try:
            # Проверка, существует ли такой файл
            studentsJSON = open('students.json').read()
        except:
            # Если нет...
            clear()
            print('Не найден файл students.json')
            input('Нажмите любую клавишу для выхода...')
        return studentsJSON

    def viewStudentList(self):
        student = Student()
        studentsJSON = student.fileChecking()
        
        # Если в studentsJSON что то есть
        # Десерилизовать данные в нем в обычный список
        if studentsJSON:
            studentlist = json.loads(studentsJSON)
        else:
            clear()
            print("students.json пуст!")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Иначе - вывод ошибки и выход

        # Перебор списка с данными студентов и вывод каждого
        i = 1
        clear()
        for student in studentlist:
            print(str(i) + " " + student)
            i += 1
        print("\nКоличество студентов: " + str(len(studentlist)))
        input("Нажмите любую клавишу для выхода...")

    def addStudent(self):
        student = Student()
        studentsJSON = student.fileChecking()

        # Если в studentsJSON что то есть
        # Десерилизовать данные в нем в обычный список
        if studentsJSON:
            studentslist = json.loads(studentsJSON)
        else:
            studentslist = []
        # Иначе - создать новый список

        clear()
        studentName = input("Имя нового студента: ")
        if len(studentName) < 3:
            print("\nИмя студента короче трех символов или пустое")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Если длина имени студента короче трех символов - вывод ошибки
            
        studentSurname = input("Фамилия нового студента: ")
        if len(studentSurname) < 3:
            print("\nФамилия студента короче трех символов или пустое")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Если длина фамилии студента короче трех символов - вывод ошибки

        # Обьединение имени и фамилии студента в одну переменную
        student = studentName + " " + studentSurname

        if student in studentslist:
            clear()
            print("Студент " + student + " уже есть в базе!")
            input("Нажмите любую клавишу для выхода...")
        else:
            studentslist.append(student)
            # Запись в конец списка нового студента

            # Запись нового значения списка в тот же файл
            open('students.json' , 'w').write(json.dumps(studentslist))
            clear()
            print("Студент " + student + " успешно добавлен в базу!")
            input("Нажмите любую клавишу для выхода...")

    def deleteStudent(self):
        student = Student()
        studentsJSON = student.fileChecking()

        # Если в studentsJSON что то есть
        # Десерилизовать данные в нем в обычный список
        if studentsJSON:
            studentslist = json.loads(studentsJSON)
        else:
            print("Файл students.json пуст!")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Иначе - вывод ошибки и выход

        clear()
        studentName = input("Имя удаляемого студента: ")
        if len(studentName) < 3:
            print("\nИмя студента короче трех символов или пустое")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Если длина имени студента короче трех символов - вывод ошибки

        studentSurname = input("Фамилия удаляемого студента: ")
        if len(studentSurname) < 3:
            print("\nФамилия студента короче трех символов или пустое")
            input("Нажмите любую клавишу для выхода...")
            exit()
        # Если длина фамилии студента короче трех символов - вывод ошибки

        # Обьединяем имя и фамилию студента
        student = studentName + " " + studentSurname

        # Попытка удалить студента из базы
        try:
            studentslist.remove(student)
            open('students.json', 'w').write(json.dumps(studentslist))
            clear()
            print("Студент " + student + " успешно удален!")
            input("Нажмите любую клавишу для выхода...")
        except:
            clear()
            print("Студент " + student + " не найден в базе")
            input("Нажмите любую клавишу для выхода...")
        # Если такого студента не существует...


student = Student()

if __name__ == "__main__":
    print("Добро пожаловать в программу StudentsLIST! \n(1 - Список студентов... 2 - Добавить студента... 3 - Удалить студента...)")

    command = int(input("\nКоманда: "))
if command == 1: # Показ списка студентов
    student.viewStudentList()
elif command == 2: # Добавление студента в базу
    student.addStudent()
elif command == 3: # Удаление студента из базы
    student.deleteStudent()