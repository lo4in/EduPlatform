from models.models import Student
from models.models import Teacher
from models.models import Admin
import os
import json
from datetime import datetime, date, timedelta
from scrap import scrape_olx_books

def load_data(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def student_find_books(subject):
    ads = scrape_olx_books(subject, pages=1)

    if not ads:
        print("Ничего не найдено")
        return

    print(f"\nРезультаты по запросу \"{subject}\":\n")
    for ad in ads[:10]:
        print(f"{ad['title']} - {ad['price']}")
        print(f"Ссылка: {ad['url']}\n")



def admin_menu(name):
    print(f"Ваше имя: {name}\nВыберите действие:\n1. Создать Пользователя\n")
    try:
        choice1 = int(input("Ваш ответ: "))
    except ValueError:
        print("Введите число!")
        return

    if choice1 == 1:
        try:
            user_name = input("Имя пользователя: ").strip()
            if not user_name:
                raise ValueError
        except ValueError:
            print("Введите корректное имя!")
            return

        try:
            user_role = int(input("Доступны роли: \n1. Admin\n2. Teacher\n3. Student\nВаш ответ: "))
        except ValueError:
            print("Введите число!")
            return

        if user_role == 1:
            user_role1 = "Admin"
        elif user_role == 2:
            user_role1 = "Teacher"
        elif user_role == 3:
            user_role1 = "Student"
        else:
            print("Нет такой роли!")
            return  

        admin = Admin(name)  
        admin.create_user(user_name, user_role1)

def teacher_menu(name):
    print(f"Ваше имя: {name}\nВыберите действие:\n1. Поставить оценки \n2. Загрузить ДЗ \n3. Загрузить Планы")
    try:
        choice1 = int(input("Ваш ответ: "))
    except ValueError:
        print("Введите число!")
        return
    if choice1 == 1:
        teacher = Teacher(name)
        sub = input("Введите предмет: ")
        st_name = input("Введите имя ученика: ")
        gr = str(input("Введите оценку (в целых числах): "))
        teacher.save_grade(sub, st_name, gr)
    elif choice1 == 2:
        teacher = Teacher(name)
        sub = input("Введите предмет: ")
        hw1 = input("Введите текст ДЗ: ")
        teacher.create_HW(sub, hw1)
    elif choice1 == 3:
        teacher = Teacher(name)
        sub = input("Введите предмет: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        plan = input("Введите текст плана: ")
        teacher.save_plan(sub, date, plan)
    else:
        print("Неправильный выбор!")

def student_menu(name):
    print(f"Ваше имя: {name}\nВыберите действие:\n1. Посмотреть оценки \n2. Посмотреть ДЗ \n3. Найти книги")
    try:
        choice1 = int(input("Ваш ответ: "))
    except ValueError:
        print("Введите число!")
        return
    if choice1 == 1:
        student = Student(name)
        sub = input("Введите предмет: ")
        student.view_grades(sub)
    elif choice1 == 2:
        student = Student(name)
        sub = input("Введите предмет: ")
        student.view_HW(sub)
    elif choice1 == 3:
        subject = input("Введите предмет для поиска книг: ")
        student_find_books(subject)

    else:
        print("Неправильный выбор!")
  


    



def menu():
    print("Здравствуйте, вас приветствует EduPlatform \n______________________________________\nВыберите кто вы:\n1. Админ\n2. Учитель\n3. Ученик\n______________________________________")
    try:
        choice1 = int(input("Ваш ответ:"))
    
    except ValueError:
        print("Ведите число!")
        return

    if choice1 == 1:
        users = load_data("/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/users.json")
        filtered_users = [i for i in users if i["role"] == "Admin"]
        try:
            name = str(input("Ваше имя: "))
        except ValueError:
            print("Введите имя!")
            return

        for u in filtered_users:
            if u["full_name"] == name:
                print("Вы вошли в аккаунт!")
                admin_menu(name)
                break
            else:
                print("Вы не админ!")
    if choice1 == 2:
        users = load_data("/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/users.json")
        filtered_users = [i for i in users if i["role"] == "Teacher"]
        try:
            name = str(input("Ваше имя: "))
        except ValueError:
            print("Введите имя!")
            return
        for u in filtered_users:
            if u["full_name"] == name:
                print("Вы вошли в аккаунт!")
                teacher_menu(name)
                break
            else:
                print("Вы не учитель!")

    if choice1 == 3:
        users = load_data("/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/users.json")
        filtered_users = [i for i in users if i["role"] == "student"]
        try:
            name = str(input("Ваше имя: "))
        except ValueError:
            print("Введите имя!")
            return
        for u in filtered_users:
            if u["full_name"] == name:
                print("Вы вошли в аккаунт!")
                student_menu(name)
                break
            else:
                print("Вы не ученик!")

               





if __name__ == "__main__":
    menu()
