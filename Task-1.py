from tkinter import *

def add_task():
    task = task_entry.get()

    if task:
        task_list.insert(END, f"Pending - {task}")
        task_entry.delete(0, END)

def update_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        task = task_list.get(index)

        if task.startswith("Pending"):
            task = task.replace("Pending", "Completed")
            task_list.delete(index)
            task_list.insert(index, task)

# Main Window
root = Tk()
root.title("To-Do List Manager")
root.geometry("450x400")

title = Label(root,text="TO-DO LIST",font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = Entry(root,width=35,font=("Arial", 12))
task_entry.pack(pady=10)

add_btn = Button(root,text="Create Task",width=15,command=add_task)
add_btn.pack(pady=5)

update_btn = Button(root,text="Update Status",width=15,command=update_task)
update_btn.pack(pady=5)

Label(root,text="Track Tasks",font=("Arial", 12, "bold")).pack(pady=10)

task_list = Listbox(root,width=50,height=12,font=("Arial", 11))
task_list.pack()

root.mainloop()
