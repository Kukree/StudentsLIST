from json import loads, dumps, JSONDecodeError
from os import system

clear = lambda: system('cls')


class Student:

    # Messages dict
    messages = {'exit': "Нажмите любую клавишу для выхода... ",
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
            students_list = open("students.json").read()
            # If there's something in students_list
            # Deserialize data to list
            if students_list:
                self.students_list = loads(students_list)
            else:
                self.students_list = []
            # Otherwise - create new list

        except FileNotFoundError:  # File not found
            print(self.messages['filenotfound'])
            input(self.messages['exit'])
            exit()
        except JSONDecodeError:  # Deserialization error
            print(self.messages['jsondecode_error'])
            input(self.messages['exit'])
            exit()
        except:
            print('unknownerror')  # Unknown error
            input(self.messages['exit'])
            exit()

    def view_student_list(self):
        # If there's something in students_list
        if self.students_list:
            student_number = 1
            clear()
            for student in self.students_list:  # Browse through the list and display each student in a new line.
                print(str(student_number) + "]" + " " + student)
                student_number += 1
            print("\nКоличество студентов: " + str(len(self.students_list)))  # Type student's count
        else:
            clear()
            print(self.messages['blankfile'])
        # Otherwise - type an error about a blank file

    def add_student(self, studentname=None, studentsurname=None):
        # Concatenate student's name and surname
        student = f"{studentname} {studentsurname}"

        if student not in self.students_list:
            # Add new element in the end of list
            self.students_list.append(student)
            clear()
            print("Студент " + student + " успешно добавлен в базу!")
        else:
            clear()
            print("Студент " + student + " уже есть в базе!")

    def delete_student(self, studentname=None, studentsurname=None):
        # Concatenate student's name and surname
        student = f"{studentname} {studentsurname}"

        # If student found
        if student in self.students_list:
            clear()
            self.students_list.remove(student)  # Delete student
            print("Студент " + student + " успешно удален из базы!")
        else:  # If student does not exist
            clear()
            print("Студент " + student + " не найден в базе")
        
    def exit(self, save=True):
        if save:  # If command to save changes is sent
            open('students.json', 'w').write(dumps(self.students_list))
            # ...serialize changes to student.json file
        exit()


if __name__ == "__main__":
    student = Student()  # Class instance
    while True:
        print("\n" * 4, "#" * 20)  # Horizontal line
        print(student.messages['commandslist'])  # Command list

        command = input(student.messages['command'])
        if command == '1':  # View list of students
            student.view_student_list()
        elif command == '2':  # Add student
            student.view_student_list()
            print("\n", "#" * 20)  # Horizontal line
            print(student.messages['studentadding'])
            student_name = input(student.messages['newstudentname'])  # Name of new student
            student.view_student_list()
            print("\nИмя: " + student_name)
            student_surname = input(student.messages['newstudentsurname'])  # Surname of new student
            student.add_student(student_name, student_surname)  # Add student
        elif command == '3':  # Delete student
            student.view_student_list()
            print("\n", "#" * 20)  # Horizontal line
            print(student.messages['studentremoving'])
            student_name = input(student.messages['deletestudentname'])  # Name of student being deleted
            student.view_student_list()
            print("\nИмя: " + student_name)
            student_surname = input(student.messages['deletestudentsurname'])  # Surname of student being deleted
            student.delete_student(student_name, student_surname)  # Delete student
        elif command == '4':  # Exit
            clear()
            print(student.messages['leaving'])
            file_checking = loads(open('students.json').read())
            if student.students_list != file_checking:  # If changed - print save suggestion
                command = input(student.messages['savechanges']).lower()
                if command == 'y':
                    student.exit()
                elif command == 'n':
                    student.exit(False)
                else:
                    clear()
                    print(student.messages['unknownvalue'])
                    input(student.messages['exit'])
                    clear()
            elif student.students_list == file_checking:  # If not changed - exit from program
                input(student.messages['exit'])
                student.exit(False)
        else:  # Unknown command
            print(student.messages['unknowncommand'])
