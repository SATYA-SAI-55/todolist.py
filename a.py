import tkinter as tk

def add_task():
    task = entry.get()
    if task:  # Only add if entry is not empty
        listbox.insert(tk.END, task)
        listbox.config(height=listbox.size())
        entry.delete(0, tk.END)

def delete_task():
    try:
        listbox.delete(listbox.curselection())
        listbox.config(height=listbox.size())
    except tk.TclError:
        pass  # Do nothing if no item is selected

# Create the main window
window = tk.Tk()
window.geometry("700x700")
window.title("To-Do List")

# Title label
title_label = tk.Label(
    window,
    text="To-Do List",
    font=("Courier", 30, "italic"),
    fg="black",
    bg="green",
    width=20,
    height=2,
    relief=tk.RAISED
)
title_label.pack(pady=20)

# Add item label
add_item_label = tk.Label(
    window,
    text="Add Items:",
    font=("Courier", 30),
    fg="blue"
)
add_item_label.place(x=10, y=150)

# Entry widget for adding tasks
entry = tk.Entry(
    window,
    font=("Courier", 25),
    fg="black"
)
entry.place(x=10, y=200)

# Add task button
add_button = tk.Button(
    window,
    text="Add Task",
    bg="orange",
    fg="black",
    font=("Courier", 14),
    command=add_task,
    relief=tk.RAISED,
    bd=5
)
add_button.place(x=420, y=200)

# Delete task button
delete_button = tk.Button(
    window,
    text="Remove",
    bg="pink",
    fg="black",
    font=("Courier", 14),
    command=delete_task,
    relief=tk.RAISED,
    bd=5
)
delete_button.place(x=550, y=200)

# Tasks label
tasks_label = tk.Label(
    window,
    text="Tasks to Do",
    font=("Courier", 30),
    fg="blue"
)
tasks_label.place(x=250, y=250)

# Listbox to display tasks
listbox = tk.Listbox(
    window,
    width=40,
    fg="black",
    font=("Courier", 20),
    bg="lightgrey"
)
listbox.place(x=10, y=320)

# Start the main event loop
window.mainloop()
