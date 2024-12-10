from sympy import Symbol, diff, integrate, limit, solve, oo, sin, exp, cos
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Text, Entry, END, filedialog, OptionMenu, StringVar, Frame
from tkinter.messagebox import showinfo

# Danh sách biểu thức có sẵn
expressions = [
    "sin(x)*exp(x)",
    "exp(x)*sin(x) + exp(x)*cos(x)",
    "sin(x**2)"
]

# Function to process the derivative
def dao_ham():
    try:
        expression = selected_expression.get()
        x = Symbol('x')
        dao_ham_result = diff(expression, x)
        ket_qua_text.delete("1.0", END)
        ket_qua_text.insert(END, f"Đạo hàm của {expression}: {dao_ham_result}\n")
    except Exception as e:
        showinfo("Lỗi", f"Lỗi tính đạo hàm: {e}")

# Function to process the indefinite integral
def nguyen_ham():
    try:
        expression = selected_expression.get()
        x = Symbol('x')
        nguyen_ham_result = integrate(expression, x)
        ket_qua_text.delete("1.0", END)
        ket_qua_text.insert(END, f"Nguyên hàm của {expression}: {nguyen_ham_result}\n")
    except Exception as e:
        showinfo("Lỗi", f"Lỗi tính nguyên hàm: {e}")

# Function to process the definite integral
def nguyen_ham_dinh():
    try:
        expression = selected_expression.get()
        x = Symbol('x')
        nguyen_ham_dinh_result = integrate(sin(x**2), (x, -oo, oo))
        ket_qua_text.delete("1.0", END)
        ket_qua_text.insert(END, f"Nguyên hàm xác định của sin(x^2) từ -∞ đến ∞: {nguyen_ham_dinh_result}\n")
    except Exception as e:
        showinfo("Lỗi", f"Lỗi tính nguyên hàm xác định: {e}")

# Function to process the limit
def gioi_han():
    try:
        expression = selected_expression.get()
        x = Symbol('x')
        gioi_han_result = limit(sin(x) / x, x, 0)
        ket_qua_text.delete("1.0", END)
        ket_qua_text.insert(END, f"Giới hạn của sin(x)/x khi x tiến đến 0: {gioi_han_result}\n")
    except Exception as e:
        showinfo("Lỗi", f"Lỗi tính giới hạn: {e}")

# Function to process the roots
def nghiem():
    try:
        x = Symbol('x')
        nghiem_result = solve(x**2 - 2, x)
        ket_qua_text.delete("1.0", END)
        ket_qua_text.insert(END, f"Nghiệm của x^2 - 2: {nghiem_result}\n")
    except Exception as e:
        showinfo("Lỗi", f"Lỗi tìm nghiệm: {e}")

# Function to plot the expression
def ve_bieu_do():
    try:
        expression = selected_expression.get()
        x = Symbol('x')
        expr = eval(expression.replace('^', '**'))  # Thay '^' bằng '**' cho phép toán mũ

        # Tạo dữ liệu để vẽ biểu đồ
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [float(expr.subs(x, val)) for val in x_vals]

        plt.plot(x_vals, y_vals, label=str(expression))
        plt.title("Biểu đồ của Biểu thức")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        showinfo("Lỗi", f"Không thể vẽ biểu đồ: {e}")

# Function to evaluate the expression at a specific point
def tinh_tai_diem():
    try:
        expression = selected_expression.get()
        diem = float(so_diem_entry.get().strip())
        x = Symbol('x')
        expr = eval(expression.replace('^', '**'))  # Thay '^' bằng '**' cho phép toán mũ
        gia_tri = float(expr.subs(x, diem))
        showinfo("Kết quả tính toán", f"Giá trị của biểu thức tại x = {diem} là {gia_tri}")
    except Exception as e:
        showinfo("Lỗi", f"Không thể tính toán biểu thức: {e}")

# Function to save results to a file
def luu_ket_qua():
    try:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Tệp văn bản", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(ket_qua_text.get("1.0", END).strip())
            showinfo("Thành công", "Kết quả đã được lưu thành công!")
    except Exception as e:
        showinfo("Lỗi", f"Không thể lưu kết quả: {e}")

# Main GUI application
def main():
    global selected_expression, ket_qua_text, so_diem_entry

    root = Tk()
    root.title("Ứng dụng Tính Toán Đại Số")
    root.geometry("800x700")

    Label(root, text="Chọn một biểu thức toán học:", font=("Arial", 12)).pack(pady=5)

    # Dropdown menu for selecting expressions
    selected_expression = StringVar(root)
    selected_expression.set(expressions[0])  # Default selection
    expression_menu = OptionMenu(root, selected_expression, *expressions)
    expression_menu.pack(pady=5)

    # Tạo Frame để chứa các nút xử lý theo hàng ngang
    button_frame = Frame(root)
    button_frame.pack(pady=10)

    # Các nút xử lý biểu thức theo hàng ngang
    Button(button_frame, text="Đạo hàm", command=dao_ham, width=15).grid(row=0, column=0, padx=5)
    Button(button_frame, text="Nguyên hàm", command=nguyen_ham, width=15).grid(row=0, column=1, padx=5)
    Button(button_frame, text="Nguyên hàm xác định", command=nguyen_ham_dinh, width=20).grid(row=0, column=2, padx=5)
    Button(button_frame, text="Giới hạn", command=gioi_han, width=15).grid(row=1, column=0, padx=5)
    Button(button_frame, text="Nghiệm", command=nghiem, width=15).grid(row=1, column=1, padx=5)
    Button(button_frame, text="Vẽ biểu đồ", command=ve_bieu_do, width=15).grid(row=1, column=2, padx=5)

    Label(root, text="Tính giá trị tại một điểm x:", font=("Arial", 12)).pack(pady=5)
    so_diem_entry = Entry(root, width=30)
    so_diem_entry.pack(pady=5)
    Button(root, text="Tính toán", command=tinh_tai_diem, width=20).pack(pady=10)

    Button(root, text="Lưu kết quả", command=luu_ket_qua, width=20).pack(pady=10)

    Label(root, text="Kết quả:", font=("Arial", 12)).pack(pady=5)

    ket_qua_text = Text(root, height=20, width=80)
    ket_qua_text.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
