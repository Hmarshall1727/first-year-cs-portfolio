import tkinter as tk

window = tk.Tk()
window.title("Student Registration")

window.mainloop()

name_label = tk.Label(
    window, text="Student Name"
)
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

course_label = tk.Label(
    window, text="Course"
)
course_label.pack()

course_entry = tk.Entry(window)
course_entry.pack()

# Later we can read:
name = name_entry.get()
course = course_entry.get()

window.mainloop()

tk.label(window, text="Name").pack(
    pady=5
)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

def register_student():
    print("Button clicked")

register_button = tk.Button(
    window,
    text="Register",
    command=register_student
)

register_button.pack()

feedback = tk.Label(window, text="")
feedback.pack()
def register_student():
    name = name_entry.get()
    feedback.config(
        text=f"Registered:{name}"
)
    
def register_student():
    name = name_entry.get().strip()
    if not name:
        feedback.config(
            text="Please enter a name"
        )
        return
    feedback.config(text=f"Registered: {name}")

course = tk.StringVar(value="Computing")
course_menu = tk.OptionMenu(
    window, course,
    "Computing", "Cyber Security",
    "Data Science"

)
course_menu.pack()

- insert missing code here

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

students = []

def register_student():
    name = name_entry.get().strip()
    if not name:
        feedback.config(text="Enter a name")
        return
student = Student(name, course.get())
students.append(student)
feedback.config(text=f"Registered: {name}")
