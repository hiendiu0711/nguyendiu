import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Dữ liệu ban đầu
list1 = ['java', 'python', 'c++', 'php', 'sql']
list2 = [4, 2, 8, 10, 6]

# Hàm tìm max và min
def find_max():
    max_val = max(4, 12, 43.3, 19, 100)
    output_var.set(f"Giá trị lớn nhất: {max_val}")

def find_min():
    min_val = min(4, 12, 43.3, 19, 100)
    output_var.set(f"Giá trị nhỏ nhất: {min_val}")

# Hàm sắp xếp theo thứ tự tăng dần hoặc giảm dần
def sort_lists(order="ascending"):
    if order == "ascending":
        list1.sort()
        list2.sort()
        output_var.set(f"Sắp xếp tăng dần:\nList1: {list1}\nList2: {list2}")
    elif order == "descending":
        list1.sort(reverse=True)
        list2.sort(reverse=True)
        output_var.set(f"Sắp xếp giảm dần:\nList1: {list1}\nList2: {list2}")

# Hàm thêm phần tử vào danh sách
def add_to_list():
    selected_list = simpledialog.askstring("Thêm phần tử", "Danh sách nào? (list1 hoặc list2):")
    if selected_list == "list1":
        element = simpledialog.askstring("Thêm phần tử", "Nhập phần tử cần thêm:")
        if element:
            list1.append(element)
            output_var.set(f"List1 sau khi thêm: {list1}")
    elif selected_list == "list2":
        try:
            element = int(simpledialog.askstring("Thêm phần tử", "Nhập phần tử cần thêm (số):"))
            list2.append(element)
            output_var.set(f"List2 sau khi thêm: {list2}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
    else:
        messagebox.showerror("Lỗi", "Danh sách không hợp lệ!")

# Hàm xóa phần tử khỏi danh sách
def remove_from_list():
    selected_list = simpledialog.askstring("Xóa phần tử", "Danh sách nào? (list1 hoặc list2):")
    if selected_list == "list1":
        element = simpledialog.askstring("Xóa phần tử", "Nhập phần tử cần xóa:")
        if element in list1:
            list1.remove(element)
            output_var.set(f"List1 sau khi xóa: {list1}")
        else:
            messagebox.showerror("Lỗi", "Phần tử không tồn tại trong List1!")
    elif selected_list == "list2":
        try:
            element = int(simpledialog.askstring("Xóa phần tử", "Nhập phần tử cần xóa (số):"))
            if element in list2:
                list2.remove(element)
                output_var.set(f"List2 sau khi xóa: {list2}")
            else:
                messagebox.showerror("Lỗi", "Phần tử không tồn tại trong List2!")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
    else:
        messagebox.showerror("Lỗi", "Danh sách không hợp lệ!")

# Hàm tìm phần tử trong danh sách
def find_element():
    selected_list = simpledialog.askstring("Tìm phần tử", "Danh sách nào? (list1 hoặc list2):")
    if selected_list == "list1":
        element = simpledialog.askstring("Tìm phần tử", "Nhập phần tử cần tìm:")
        if element in list1:
            output_var.set(f"'{element}' tồn tại trong List1.")
        else:
            output_var.set(f"'{element}' không có trong List1.")
    elif selected_list == "list2":
        try:
            element = int(simpledialog.askstring("Tìm phần tử", "Nhập phần tử cần tìm (số):"))
            if element in list2:
                output_var.set(f"{element} tồn tại trong List2.")
            else:
                output_var.set(f"{element} không có trong List2.")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
    else:
        messagebox.showerror("Lỗi", "Danh sách không hợp lệ!")

# Hàm đếm số phần tử trong danh sách
def count_elements():
    selected_list = simpledialog.askstring("Đếm phần tử", "Danh sách nào? (list1 hoặc list2):")
    if selected_list == "list1":
        count = len(list1)
        output_var.set(f"Số phần tử trong List1: {count}")
    elif selected_list == "list2":
        count = len(list2)
        output_var.set(f"Số phần tử trong List2: {count}")
    else:
        messagebox.showerror("Lỗi", "Danh sách không hợp lệ!")

# Hàm xóa tất cả các phần tử trong danh sách
def clear_list():
    selected_list = simpledialog.askstring("Xóa tất cả", "Danh sách nào? (list1 hoặc list2):")
    if selected_list == "list1":
        list1.clear()
        output_var.set(f"List1 đã được xóa tất cả các phần tử.")
    elif selected_list == "list2":
        list2.clear()
        output_var.set(f"List2 đã được xóa tất cả các phần tử.")
    else:
        messagebox.showerror("Lỗi", "Danh sách không hợp lệ!")

# Hàm lưu danh sách vào file
def save_to_file():
    try:
        with open("lists.txt", "w") as file:
            file.write(f"List1: {list1}\n")
            file.write(f"List2: {list2}\n")
        output_var.set("Danh sách đã được lưu vào file lists.txt")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lưu danh sách: {e}")

# Giao diện chính
root = tk.Tk()
root.title("Quản lý danh sách")
root.geometry("400x600")
root.resizable(False, False)

# Các biến hiển thị
output_var = tk.StringVar(value="Kết quả sẽ hiển thị ở đây.")

# Khung hiển thị danh sách
frame_lists = tk.Frame(root)
frame_lists.pack(pady=10)

list1_var = tk.StringVar(value=f"List1: {list1}")
list2_var = tk.StringVar(value=f"List2: {list2}")

tk.Label(frame_lists, textvariable=list1_var).pack()
tk.Label(frame_lists, textvariable=list2_var).pack()

# Khung chứa các nút
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Tìm Max", width=15, command=find_max).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Tìm Min", width=15, command=find_min).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Sắp xếp tăng", width=15, command=lambda: sort_lists("ascending")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Sắp xếp giảm", width=15, command=lambda: sort_lists("descending")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Thêm phần tử", width=15, command=add_to_list).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Xóa phần tử", width=15, command=remove_from_list).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Tìm phần tử", width=15, command=find_element).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Đếm phần tử", width=15, command=count_elements).grid(row=3, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Xóa tất cả phần tử", width=15, command=clear_list).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Lưu danh sách", width=15, command=save_to_file).grid(row=4, column=1, padx=5, pady=5)

# Khung hiển thị kết quả
frame_output = tk.Frame(root)
frame_output.pack(pady=10, fill="x")

tk.Label(frame_output, text="Kết quả:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
tk.Label(frame_output, textvariable=output_var, wraplength=380, justify="left", bg="#f0f0f0", relief="sunken").pack(padx=10, pady=5, fill="x")

root.mainloop()
