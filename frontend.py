import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests

API_URL = "http://127.0.0.1:8000/api/todos/"

class TaskApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("1500x1020") 
        ctk.set_appearance_mode("dark")  

        self.selected_task_id = None  

        # Load Background Image
        self.bg_image = Image.open("bg_image.jpg")  
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Background Label
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Main Frame (Transparent)
        self.main_frame = ctk.CTkFrame(self, fg_color=None)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Label (Transparent)
        self.title_label = ctk.CTkLabel(self.main_frame, text="Tasks List", font=("Pacifico", 36), fg_color=None)
        self.title_label.pack(pady=5)

        # Task Listbox (Matching Background)
        self.task_listbox = tk.Listbox(self.main_frame, height=15, width=75, font=("Arial", 18), 
                                       bg="#1e1e1e", fg="white", borderwidth=0, highlightthickness=0)
        self.task_listbox.pack(pady=5)
        self.task_listbox.bind("<ButtonRelease-1>", self.load_selected_task)

        # Task Entry (Matching Background)
        self.title_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Task Name", 
                                        font=("Arial", 18), width=300, height=50, 
                                        fg_color="#333333", border_width=0, text_color="white")
        self.title_entry.pack(pady=5)

        # Description Entry
        self.desc_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Description", 
                                       font=("Arial", 18), width=300, height=50,   
                                       fg_color="#333333", border_width=0, text_color="white")
        self.desc_entry.pack(pady=5)

        # Completed Checkbox (Transparent)
        self.completed_var = tk.BooleanVar()
        self.completed_checkbox = ctk.CTkCheckBox(self.main_frame, text="Completed", variable=self.completed_var, 
                                                  font=("Pacifico", 18), fg_color=None)
        self.completed_checkbox.pack(pady=5)

        # Buttons Frame (Transparent)
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color=None)
        self.button_frame.pack(pady=10)

        # Buttons
        button_style = {"width": 200, "height": 50, "font": ("Pacifico", 18)}

        self.add_button = ctk.CTkButton(self.button_frame, text="Add Task", command=self.add_task, 
                                        fg_color="#3b82f6", hover_color="#2563eb", **button_style)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ctk.CTkButton(self.button_frame, text="Update Task", command=self.update_task, 
                                           fg_color="#3b82f6", hover_color="#2563eb", **button_style)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete Task", command=self.delete_task, 
                                           fg_color="#ef4444", hover_color="#dc2626", **button_style)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.refresh_button = ctk.CTkButton(self.button_frame, text="Refresh List", command=self.load_tasks, 
                                            fg_color="#3b82f6", hover_color="#2563eb", **button_style)
        self.refresh_button.grid(row=0, column=3, padx=5, pady=5)

        # Load tasks initially
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        response = requests.get(API_URL)
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                status = "(✔)" if task["completed"] else "(✖)"
                self.task_listbox.insert(tk.END, f"{task['id']}. {task['title']} - {task['description']} {status}")

    def load_selected_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index[0])
            task_id = task_text.split(".")[0]  # Extract task ID
            response = requests.get(f"{API_URL}{task_id}/")
            if response.status_code == 200:
                task = response.json()
                self.selected_task_id = task["id"]
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, task["title"])
                self.desc_entry.delete(0, tk.END)
                self.desc_entry.insert(0, task["description"])
                self.completed_var.set(task["completed"])

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        completed = self.completed_var.get()
        if title and desc:
            data = {"title": title, "description": desc, "completed": completed}
            requests.post(API_URL, json=data)
            self.load_tasks()

    def update_task(self):
        if self.selected_task_id:
            title = self.title_entry.get()
            desc = self.desc_entry.get()
            completed = self.completed_var.get()
            data = {"title": title, "description": desc, "completed": completed}
            requests.put(f"{API_URL}{self.selected_task_id}/", json=data)
            self.load_tasks()
            self.selected_task_id = None  

    def delete_task(self):
        if self.selected_task_id:
            requests.delete(f"{API_URL}{self.selected_task_id}/")
            self.load_tasks()
            self.selected_task_id = None

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()
