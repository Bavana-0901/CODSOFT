import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()
    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")

# Refresh List
def refresh_list(data=None):
    contact_listbox.delete(0, tk.END)

    if data is None:
        data = contacts

    for contact in data:
        contact_listbox.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']}"
        )

# Search Contact
def search_contact():
    keyword = search_entry.get().lower()

    result = [
        c for c in contacts
        if keyword in c["name"].lower()
        or keyword in c["phone"]
    ]

    refresh_list(result)

# Display Selected Contact
def show_contact(event):
    selected = contact_listbox.curselection()

    if not selected:
        return

    index = selected[0]
    contact = contacts[index]

    clear_fields()

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    address_entry.insert("1.0", contact["address"])

# Update Contact
def update_contact():
    selected = contact_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first!")
        return

    index = selected[0]

    contacts[index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get("1.0", tk.END).strip()
    }

    save_contacts()
    refresh_list()
    messagebox.showinfo("Success", "Contact Updated!")

# Delete Contact
def delete_contact():
    selected = contact_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first!")
        return

    index = selected[0]

    del contacts[index]

    save_contacts()
    refresh_list()
    clear_fields()

    messagebox.showinfo("Success", "Contact Deleted!")

# Clear Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")
root.resizable(False, False)


ROOT_BG = "Lavender"
HEADER_BG = "Blue"
HEADER_FG = "White"
LABEL_FG = "Black"
ENTRY_BG = "White"
ENTRY_FG = "Black"
LIST_BG = "LightYellow"
SELECT_BG = "Gold"

root.configure(bg=ROOT_BG)

contacts = load_contacts()

# Header
tk.Label(root, text="Contact Book", bg=HEADER_BG, fg=HEADER_FG, font=("Segoe UI", 18, "bold")).place(x=0, y=0, relwidth=1, height=60)

# Search Section (shifted down for header)
tk.Label(root, text="Search", bg=ROOT_BG, fg=LABEL_FG).place(x=20, y=70)

search_entry = tk.Entry(root, width=25, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
search_entry.place(x=80, y=70)

def _make_button(parent, text, cmd, x, y, bg, hover, fg="white", width=10):
    b = tk.Button(parent, text=text, command=cmd, bg=bg, fg=fg, activebackground=hover, relief=tk.FLAT)
    b.place(x=x, y=y)
    def on_enter(e):
        b['bg'] = hover
    def on_leave(e):
        b['bg'] = bg
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)
    return b

_make_button(root, "Search", search_contact, 250, 67, "Orange", "orange", fg="black")
_make_button(root, "Show All", lambda: refresh_list(), 320, 67, "Brown", "Brown", fg="black")

# Contact List with scrollbar
contact_listbox = tk.Listbox(root, width=40, height=18, bg=LIST_BG, fg=ENTRY_FG, selectbackground=SELECT_BG, activestyle='none')
contact_listbox.place(x=20, y=110)
contact_listbox.bind("<<ListboxSelect>>", show_contact)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=contact_listbox.yview)
scrollbar.place(x=320, y=110, height=290)
contact_listbox.config(yscrollcommand=scrollbar.set)

# Labels and Entries (moved down)
tk.Label(root, text="Name", bg=ROOT_BG, fg=LABEL_FG).place(x=380, y=110)
name_entry = tk.Entry(root, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
name_entry.place(x=460, y=110)

tk.Label(root, text="Phone", bg=ROOT_BG, fg=LABEL_FG).place(x=380, y=150)
phone_entry = tk.Entry(root, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
phone_entry.place(x=460, y=150)

tk.Label(root, text="Email", bg=ROOT_BG, fg=LABEL_FG).place(x=380, y=190)
email_entry = tk.Entry(root, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
email_entry.place(x=460, y=190)

tk.Label(root, text="Address", bg=ROOT_BG, fg=LABEL_FG).place(x=380, y=230)
address_entry = tk.Text(root, width=22, height=5, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
address_entry.place(x=460, y=230)

# Buttons (colored)
_make_button(root, "Add Contact", add_contact, 400, 340, "Green", "Green", fg="white")
_make_button(root, "Update Contact", update_contact, 530, 340, "Blue", "Blue", fg="white")
_make_button(root, "Delete Contact", delete_contact, 400, 385, "Red", "Red", fg="white")
_make_button(root, "Clear", clear_fields, 530, 385, "Gold", "Gold", fg="Gray")

refresh_list()

root.mainloop()