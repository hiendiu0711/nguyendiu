import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog, ttk, Entry, Frame
from tkinter.messagebox import showinfo


# Function to load data
def load_data():
  global df, class_filter
  filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
  if filepath:
    try:
      df = pd.read_csv(filepath, index_col=0, header=0)
      showinfo("Thành công", "Dữ liệu đã được tải thành công!")
      update_class_filter()
    except Exception as e:
      showinfo("Lỗi", f"Không thể tải dữ liệu: {e}")


def update_class_filter():
  global df
  if df is not None:
    classes = df.iloc[:, 0].unique()  # Assuming class information is in the first column
    class_filter["values"] = ["Tất cả"] + list(classes)
    class_filter.current(0)


# Function to plot data
def plot_data():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  selected_class = class_filter.get()
  filtered_df = df

  if selected_class != "Tất cả":
    filtered_df = df[df.iloc[:, 0] == selected_class]

  in_data = np.array(filtered_df.iloc[:, :])
  diemA = in_data[:, 2]
  diemBc = in_data[:, 3]

  plt.plot(range(len(diemA)), diemA, 'r-', label="Điểm 9-10 (A)")
  plt.plot(range(len(diemBc)), diemBc, 'g-', label="Điểm 1-8 (B)")
  plt.xlabel('Lớp')
  plt.ylabel('Số sinh viên đạt điểm')
  plt.legend(loc='upper right')
  plt.title(f"Điểm cho {'Tất cả các lớp' if selected_class == 'Tất cả' else selected_class}")
  plt.show()


# Function to save filtered data
def save_filtered_data():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  selected_class = class_filter.get()
  filtered_df = df

  if selected_class != "Tất cả":
    filtered_df = df[df.iloc[:, 0] == selected_class]

  save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
  if save_path:
    try:
      filtered_df.to_csv(save_path)
      showinfo("Thành công", "Dữ liệu đã được lưu thành công!")
    except Exception as e:
      showinfo("Lỗi", f"Không thể lưu dữ liệu: {e}")


# Function to calculate total students per class and overall
def calculate_totals():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  selected_class = class_filter.get()

  if selected_class == "Tất cả":
    total_students = len(df)
    total_A = len(df[(df.iloc[:, 2] >= 9) & (df.iloc[:, 2] <= 10)])  # Điểm 9-10 (A)
    total_Bplus = len(df[(df.iloc[:, 2] >= 1) & (df.iloc[:, 2] <= 8)])  # Điểm 1-8 (B)
    result_label.config(text=f"Tổng số sinh viên ở tất cả các lớp: {total_students}\n"
                             f"Tổng số sinh viên đạt điểm 9-10 (A): {total_A}\nTổng số sinh viên đạt điểm 1-8 (B): {total_Bplus}")
  else:
    # Filter by selected class
    filtered_df = df[df.iloc[:, 0] == selected_class]
    total_students = len(filtered_df)
    total_A = len(filtered_df[(filtered_df.iloc[:, 2] >= 9) & (filtered_df.iloc[:, 2] <= 10)])
    total_Bplus = len(filtered_df[(filtered_df.iloc[:, 2] >= 1) & (filtered_df.iloc[:, 2] <= 8)])
    result_label.config(text=f"Tổng số sinh viên ở lớp {selected_class}: {total_students}\n"
                             f"Tổng số sinh viên đạt điểm 9-10 (A): {total_A}\nTổng số sinh viên đạt điểm 1-8 (B): {total_Bplus}")


# Function to find and display the top student
def find_top_student():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  # Find the student with the highest score
  top_student_df = df[df.iloc[:, 2] == df.iloc[:, 2].max()]  # Find the student with the highest score (Điểm A: 9-10)

  if not top_student_df.empty:
    top_student_name = top_student_df.iloc[0, 0]  # Assuming the student's name is in the first column
    top_student_score = top_student_df.iloc[0, 2]  # Assuming score is in the 3rd column
    result_label.config(text=f"Sinh viên có điểm cao nhất là: {top_student_name}\nĐiểm: {top_student_score}")
  else:
    result_label.config(text="Không tìm thấy sinh viên với điểm cao nhất.")


# Function to find students by a specific score
def find_students_by_score():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  try:
    target_score = float(score_input.get())
    filtered_students = df[df.iloc[:, 2] == target_score]

    if not filtered_students.empty:
      student_names = "\n".join(filtered_students.iloc[:, 0])
      result_label.config(text=f"Sinh viên có điểm {target_score}:\n{student_names}")
    else:
      result_label.config(text=f"Không có sinh viên nào đạt điểm {target_score}.")
  except ValueError:
    showinfo("Lỗi", "Vui lòng nhập một số điểm hợp lệ!")


# Function to find the highest score per class and display students
def find_highest_scores_per_class():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  result = []
  classes = df.iloc[:, 0].unique()  # Lấy danh sách lớp

  for class_name in classes:
    class_df = df[df.iloc[:, 0] == class_name]  # Lọc dữ liệu theo lớp
    max_score = class_df.iloc[:, 2].max()  # Tìm điểm cao nhất
    top_students = class_df[class_df.iloc[:, 2] == max_score]  # Lọc sinh viên đạt điểm cao nhất
    student_names = ", ".join(top_students.iloc[:, 1])  # Lấy danh sách tên sinh viên

    result.append(f"Lớp {class_name}:\n- Điểm cao nhất: {max_score}\n- Sinh viên: {student_names}")

  result_label.config(text="\n\n".join(result))


# Function to calculate total score and average score per class and overall
def calculate_total_and_average():
  if df is None:
    showinfo("Lỗi", "Vui lòng tải dữ liệu trước!")
    return

  selected_class = class_filter.get()
  result = ""

  if selected_class == "Tất cả":
    total_score = df.iloc[:, 2].sum()  # Tổng điểm
    average_score = df.iloc[:, 2].mean()  # Điểm trung bình
    result = f"Tổng điểm tất cả sinh viên: {total_score}\nĐiểm trung bình: {average_score:.2f}"
  else:
    filtered_df = df[df.iloc[:, 0] == selected_class]
    total_score = filtered_df.iloc[:, 2].sum()
    average_score = filtered_df.iloc[:, 2].mean()
    result = f"Tổng điểm lớp {selected_class}: {total_score}\nĐiểm trung bình lớp {selected_class}: {average_score:.2f}"

  result_label.config(text=result)


# Main GUI application
def main():
  global class_filter, df, result_label, score_input
  df = None

  root = Tk()
  root.title("Giao diện quản lý điểm sinh viên")
  root.geometry("500x700")

  # Title
  Label(root, text="Quản lý và hiển thị dữ liệu điểm sinh viên", font=("Arial", 16)).pack(pady=10)

  # Data Loading
  Button(root, text="Tải Dữ Liệu", command=load_data, width=20).pack(pady=5)

  # Filter by Class
  filter_frame = Frame(root)
  filter_frame.pack(pady=10, fill="x")

  Label(filter_frame, text="Lọc theo lớp:", font=("Arial", 12)).pack(side="left", padx=10)
  class_filter = ttk.Combobox(filter_frame, state="readonly", width=30)
  class_filter.pack(side="left", padx=10)

  # Input Score
  score_frame = Frame(root)
  score_frame.pack(pady=10, fill="x")

  Label(score_frame, text="Nhập số điểm:", font=("Arial", 12)).pack(side="left", padx=10)
  score_input = Entry(score_frame, width=10)
  score_input.pack(side="left", padx=10)

  Button(score_frame, text="Tìm Sinh Viên", command=find_students_by_score, width=15).pack(side="left", padx=10)

  # Buttons for Actions
  Button(root, text="Hiển thị Dữ Liệu", command=plot_data, width=20).pack(pady=5)
  Button(root, text="Tính Tổng Sinh Viên", command=calculate_totals, width=20).pack(pady=5)
  Button(root, text="Tìm Sinh Viên Có Điểm Cao Nhất", command=find_top_student, width=25).pack(pady=5)
  Button(root, text="Điểm Cao Nhất Mỗi Lớp", command=find_highest_scores_per_class, width=25).pack(pady=5)

  # New button to calculate total score and average score
  Button(root, text="Tính Tổng và Điểm Trung Bình", command=calculate_total_and_average, width=25).pack(pady=5)

  # Result Display
  result_label = Label(root, text="", font=("Arial", 12), justify="left", anchor="w", bg="white", wraplength=480)
  result_label.pack(pady=10, padx=10, fill="both", expand=True)

  # Save Data Button
  Button(root, text="Lưu Dữ Liệu Đã Lọc", command=save_filtered_data, width=20).pack(pady=10)

  root.mainloop()


if __name__ == "__main__":
  main()
