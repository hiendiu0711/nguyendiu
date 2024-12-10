import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Dữ liệu ban đầu
listl = ['java', 'python', 'c++', 'php', 'sql']
list2 = [4, 2, 8, 10, 6]

# Các hàm chức năng
def find_max_min():
    max_val = max(4, 12, 43.3, 19, 100)
    min_val = min(4, 12, 43.3, 19, 100)
    messagebox.showinfo("Max/Min", f"Maximum: {max_val}\nMinimum: {min_val}")

def sort_lists():
    listl.sort()
    list2.sort()
    listl_var.set(f"List1: {listl}")
    list2_var.set(f"List2: {list2}")
    messagebox.showinfo("Sort", "Lists have been sorted!")

def add_to_list():
    selected_list = simpledialog.askstring("Add Element", "Which list? (list1 or list2):")
    if selected_list == "list1":
        element = simpledialog.askstring("Add Element", "Enter the element to add:")
        if element:
            listl.append(element)
            listl_var.set(f"List1: {listl}")
    elif selected_list == "list2":
        try:
            element = int(simpledialog.askstring("Add Element", "Enter the element to add:"))
            list2.append(element)
            list2_var.set(f"List2: {list2}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    else:
        messagebox.showerror("Error", "Invalid list selection!")

def remove_from_list():
    selected_list = simpledialog.askstring("Remove Element", "Which list? (list1 or list2):")
    if selected_list == "list1":
        element = simpledialog.askstring("Remove Element", "Enter the element to remove:")
        if element in listl:
            listl.remove(element)
            listl_var.set(f"List1: {listl}")
        else:
            messagebox.showerror("Error", "Element not found in list1!")
    elif selected_list == "list2":
        try:
            element = int(simpledialog.askstring("Remove Element", "Enter the element to remove:"))
            if element in list2:
                list2.remove(element)
                list2_var.set(f"List2: {list2}")
            else:
                messagebox.showerror("Error", "Element not found in list2!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    else:
        messagebox.showerror("Error", "Invalid list selection!")

def save_to_file():
    try:
        with open("lists.txt", "w") as file:
            file.write(f"List1: {listl}\n")
            file.write(f"List2: {list2}\n")
        messagebox.showinfo("Save", "Lists have been saved to lists.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save lists: {e}")

# Giao diện chính
root = tk.Tk()
root.title("List Operations")

listl_var = tk.StringVar(value=f"List1: {listl}")
list2_var = tk.StringVar(value=f"List2: {list2}")

# Hiển thị danh sách
tk.Label(root, textvariable=listl_var).pack()
tk.Label(root, textvariable=list2_var).pack()

# Các nút chức năng
tk.Button(root, text="Find Max/Min", command=find_max_min).pack(pady=5)
tk.Button(root, text="Sort Lists", command=sort_lists).pack(pady=5)
tk.Button(root, text="Add to List", command=add_to_list).pack(pady=5)
tk.Button(root, text="Remove from List", command=remove_from_list).pack(pady=5)
tk.Button(root, text="Save to File", command=save_to_file).pack(pady=5)

root.mainloop()
