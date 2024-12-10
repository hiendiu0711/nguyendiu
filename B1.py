import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Giải Hệ Phương Trình")

    def check_invertibility():
        try:
            A = np.array([(1, 2), (3, 4)])
            det_A = np.linalg.det(A)
            messagebox.showinfo("Kết quả", f"Định thức của A: {det_A}\n{'Ma trận không khả nghịch.' if det_A == 0 else 'Ma trận khả nghịch.'}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def solve_system():
        try:
            A = np.array([(1, 2), (3, 4)])
            B = np.array([5, 6])
            det_A = np.linalg.det(A)
            if det_A == 0:
                messagebox.showerror("Lỗi", "Ma trận không khả nghịch.")
                return

            A1 = np.linalg.inv(A)
            X = np.dot(A1, B)
            messagebox.showinfo("Nghiệm", f"Nghiệm của hệ: {X}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def plot_solution():
        try:
            A = np.array([(1, 2), (3, 4)])
            B = np.array([5, 6])
            det_A = np.linalg.det(A)
            if det_A == 0:
                messagebox.showerror("Lỗi", "Không thể vẽ đồ thị vì ma trận không khả nghịch.")
                return

            A1 = np.linalg.inv(A)
            X = np.dot(A1, B)

            if A.shape == (2, 2) and len(B) == 2:
                x = np.linspace(-10, 10, 400)

                y1 = (B[0] - A[0, 0] * x) / A[0, 1]
                y2 = (B[1] - A[1, 0] * x) / A[1, 1]

                plt.plot(x, y1, label="Phương trình 1")
                plt.plot(x, y2, label="Phương trình 2")
                plt.scatter(X[0], X[1], color='red', label="Nghiệm", zorder=5)

                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.grid(color='gray', linestyle='--', linewidth=0.5)
                plt.legend()
                plt.title("Đồ thị hệ phương trình")
                plt.show()
            else:
                messagebox.showerror("Lỗi", "Không thể vẽ đồ thị vì hệ không ở dạng 2D.")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    btn_check = tk.Button(root, text="Kiểm tra khả nghịch", command=check_invertibility)
    btn_check.pack(pady=10)

    btn_solve = tk.Button(root, text="Giải hệ phương trình", command=solve_system)
    btn_solve.pack(pady=10)

    btn_plot = tk.Button(root, text="Vẽ đồ thị nghiệm", command=plot_solution)
    btn_plot.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
