import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

# Mảng dữ liệu (ban đầu để trống, sẽ cập nhật từ đầu vào người dùng)
arr = None

# Hàm xử lý nhập mảng từ người dùng
def input_array():
    global arr
    try:
        user_input = array_input.get("1.0", tk.END).strip()
        arr = np.array(eval(user_input))
        array_label.config(text=str(arr))
        output_field.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Array updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid array input: {e}")

# Các hàm thực hiện từng chức năng (như cũ)
def largest_element():
    return f"Largest element is: {arr.max()}"

def row_wise_max():
    return f"Row-wise maximum elements: {arr.max(axis=1)}"

def column_wise_min():
    return f"Column-wise minimum elements: {arr.min(axis=0)}"

def total_sum():
    return f"Sum of all array elements: {arr.sum()}"

def cumulative_sum():
    return f"Cumulative sum along each row:\n{arr.cumsum(axis=1)}"

def column_range():
    col_max = arr.max(axis=0)
    col_min = arr.min(axis=0)
    col_range = col_max - col_min
    return f"Column-wise range (max - min): {col_range}"

def largest_position():
    largest_value = arr.max()
    largest_position = np.unravel_index(np.argmax(arr), arr.shape)
    return f"Largest value: {largest_value}\nPosition (row, column): {largest_position}"

def normalize_array():
    normalized = (arr - arr.min()) / (arr.max() - arr.min())
    return f"Normalized Array:\n{normalized}"

def show_all_results():
    if arr is None:
        messagebox.showerror("Error", "Array is not defined!")
        return
    results = [
        largest_element(),
        row_wise_max(),
        column_wise_min(),
        total_sum(),
        cumulative_sum(),
        column_range(),
        largest_position(),
        normalize_array()
    ]
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, "\n\n".join(results))

def reset():
    output_field.delete("1.0", tk.END)

def save_to_file():
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Results As"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(output_field.get("1.0", tk.END))
            messagebox.showinfo("Success", f"Results saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save results: {e}")

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Array Operations")

# Nhập mảng
ttk.Label(root, text="Enter Array (e.g., [[1, 2], [3, 4]]):", font=("Arial", 12, "bold")).pack(pady=5)
array_input = tk.Text(root, height=3, width=40)
array_input.pack(pady=5)
ttk.Button(root, text="Update Array", command=input_array).pack(pady=5)

# Nhãn hiển thị mảng
ttk.Label(root, text="Array Data:", font=("Arial", 12, "bold")).pack(pady=5)
array_label = ttk.Label(root, text="Array not defined", font=("Courier", 12), relief="solid")
array_label.pack(pady=5)

# Các nút thực hiện chức năng
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Largest Element", command=lambda: output_field.insert(tk.END, largest_element() + "\n")).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Row-wise Max", command=lambda: output_field.insert(tk.END, row_wise_max() + "\n")).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Column-wise Min", command=lambda: output_field.insert(tk.END, column_wise_min() + "\n")).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="Total Sum", command=lambda: output_field.insert(tk.END, total_sum() + "\n")).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Cumulative Sum", command=lambda: output_field.insert(tk.END, cumulative_sum() + "\n")).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Column Range", command=lambda: output_field.insert(tk.END, column_range() + "\n")).grid(row=1, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="Largest Position", command=lambda: output_field.insert(tk.END, largest_position() + "\n")).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Normalize Array", command=lambda: output_field.insert(tk.END, normalize_array() + "\n")).grid(row=2, column=1, padx=5, pady=5)

# Nút Show All Results
ttk.Button(button_frame, text="Show All Results", command=show_all_results).grid(row=2, column=2, padx=5, pady=5)

# Nút Reset và Save
ttk.Button(button_frame, text="Reset", command=reset).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Save Results", command=save_to_file).grid(row=3, column=2, padx=5, pady=5)

# Nhãn và ô hiển thị kết quả
ttk.Label(root, text="Results:", font=("Arial", 12, "bold")).pack(pady=5)
output_field = tk.Text(root, height=15, width=60, state=tk.NORMAL)
output_field.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
