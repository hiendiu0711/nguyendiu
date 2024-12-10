import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Text, END, messagebox


# Tạo hàm chính để thực hiện từng chức năng
def calculate_determinant():
    det = np.linalg.det(A)
    output_text.insert(END, f"Định thức của A: {det}\n")
    if det == 0:
        messagebox.showwarning("Thông báo", "Ma trận A không khả nghịch!")


def calculate_inverse():
    if np.linalg.det(A) == 0:
        messagebox.showwarning("Thông báo", "Không thể tính nghịch đảo vì A không khả nghịch!")
    else:
        inverse = np.linalg.inv(A)
        output_text.insert(END, f"Ma trận nghịch đảo của A:\n{inverse}\n")


def solve_equations():
    if np.linalg.det(A) == 0:
        messagebox.showwarning("Thông báo", "Không thể giải hệ phương trình vì A không khả nghịch!")
    else:
        solution = np.linalg.solve(A, B)
        output_text.insert(END, f"Nghiệm của hệ phương trình: {solution}\n")


def plot_solution():
    if np.linalg.det(A) == 0:
        messagebox.showwarning("Thông báo", "Không thể vẽ đồ thị nghiệm vì A không khả nghịch!")
    else:
        solution = np.linalg.solve(A, B)
        plt.figure(figsize=(6, 4))
        plt.bar(['X1', 'X2'], solution, color=['blue', 'orange'], alpha=0.7)
        plt.title("Đồ thị nghiệm của hệ phương trình")
        plt.xlabel("Biến số")
        plt.ylabel("Giá trị nghiệm")
        plt.grid(True, axis='y', linestyle='--', alpha=0.6)
        plt.show()


def calculate_norm():
    norm = np.linalg.norm(A)
    output_text.insert(END, f"Chuẩn (norm) của A: {norm}\n")


def show_transpose():
    transpose = A.T
    output_text.insert(END, f"Ma trận chuyển vị của A:\n{transpose}\n")


# Tạo giao diện GUI
root = Tk()
root.title("Giải hệ phương trình tuyến tính")
root.geometry("600x500")

# Khởi tạo ma trận A và vector B
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])

# Tiêu đề
Label(root, text="Giải Hệ Phương Trình Tuyến Tính", font=("Arial", 16)).pack(pady=10)

# Các nút chức năng
Button(root, text="Tính định thức", command=calculate_determinant, width=20).pack(pady=5)
Button(root, text="Tính ma trận nghịch đảo", command=calculate_inverse, width=20).pack(pady=5)
Button(root, text="Giải hệ phương trình", command=solve_equations, width=20).pack(pady=5)
Button(root, text="Vẽ đồ thị nghiệm", command=plot_solution, width=20).pack(pady=5)
Button(root, text="Tính chuẩn ma trận", command=calculate_norm, width=20).pack(pady=5)
Button(root, text="Hiển thị chuyển vị", command=show_transpose, width=20).pack(pady=5)

# Vùng hiển thị kết quả
Label(root, text="Kết quả:", font=("Arial", 14)).pack(pady=10)
output_text = Text(root, height=10, width=70)
output_text.pack()

# Chạy ứng dụng
root.mainloop()
