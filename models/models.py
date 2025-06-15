import json
import os



def load_data(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(path, users_list):
    os.makedirs(os.path.dirname(path), exist_ok=True) 
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users_list, f, indent=4)


class User:
    def __init__(self, full_name, role):
        self.full_name = full_name
        self.role = role

    def Dict(self):
        return {
            "full_name": self.full_name,
            "role": self.role,
        }

    def show_user(self):
        print(self.Dict())


class Admin(User):
    def __init__(self, full_name, role="Admin"):
        super().__init__(full_name, role)

    def show_user(self):
        print(self.full_name, self.role)

    def create_user(self, full_name, role, json_path="/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/users.json"):
        new_user = User(full_name, role)
        users = load_data(json_path)
        users.append(new_user.Dict())
        save_data(json_path, users)
        print(f"Пользователь {full_name} успешно создан и сохранён.")
        return new_user


class Teacher(User):
    def __init__(self, full_name, role="Teacher"):
        super().__init__(full_name, role)

    def show_user(self):
        print(self.full_name, self.role)

    def grades(self, subject, student_name, grade):
        return {
            "subject": subject,
            "student": student_name,
            "grade": grade,
            "teacher": self.full_name
        }
    def save_grade(self, subject, student_name, grade, json_path="/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/grades.json"):
        new_grade = self.grades(subject, student_name, grade)
        grades = load_data(json_path)
        grades.append(new_grade)
        save_data(json_path, grades)
        print(f"Оценка для {student_name} по {subject}: {grades[-1]} — сохранена.")
        return new_grade

    def HW(self, subject, hw_text):
        return {
            "Teacher": self.full_name,
            "Subject": subject,
            "HW": hw_text
        }
    def create_HW(self, subject, hw_text, json_path="/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/hw.json"):
        new_hw = self.HW(subject, hw_text)
        hws = load_data(json_path)
        hws.append(new_hw)
        save_data(json_path, hws)
        print(f"ДЗ по {subject}: '{hw_text}' — успешно сохранено.")
        return new_hw

    def plans(self, subject, date, topic):
        return {
            "teacher": self.full_name,
            "subject": subject,
            "Date": date,
            "topic": topic,
        }
    def save_plan(self, subject, date, topic, json_path="/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/plans.json"):
        new_plan = self.plans(subject, date, topic)
        plans = load_data(json_path)
        plans.append(new_plan)
        save_data(json_path, plans)
        print(f"План урока по {subject} на {date} — сохранён.")
        return new_plan

class Student(User):
    def __init__(self, full_name, role="Student"):
        super().__init__(full_name, role)

    def show_user(self):
        print(self.full_name, self.role)

    def view_grades(self, subject):
        grades = load_data("/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/grades.json")
        subject = subject
        filtered_grades = [g for g in grades if g["subject"] == subject]
        filtered_names = [g for g in grades if g["student"] == self.full_name]

        for name in filtered_names:
            print(name)
        
        for grade in filtered_grades:
            print(grade)
    def view_HW(self, subject):
        homeworks = load_data("/Users/lochinbek/Desktop/BIandAI/EduPlatform/data/hw.json")


        subject = subject
        filtered_hw = [hw for hw in homeworks if hw["subject"] == subject]

        
        for hw in filtered_hw:
            print(hw)
    
        



