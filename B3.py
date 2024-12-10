import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog, ttk
from tkinter.messagebox import showinfo

# Function to load data
def load_data():
    global df, class_filter
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        try:
            df = pd.read_csv(filepath, index_col=0, header=0)
            showinfo("Success", "Data loaded successfully!")
            update_class_filter()
        except Exception as e:
            showinfo("Error", f"Failed to load data: {e}")

def update_class_filter():
    global df
    if df is not None:
        classes = df.iloc[:, 0].unique()  # Assuming class information is in the first column
        class_filter["values"] = ["All"] + list(classes)
        class_filter.current(0)

# Function to plot data
def plot_data():
    if df is None:
        showinfo("Error", "Please load data first!")
        return

    selected_class = class_filter.get()
    filtered_df = df

    if selected_class != "All":
        filtered_df = df[df.iloc[:, 0] == selected_class]

    in_data = np.array(filtered_df.iloc[:, :])
    diemA = in_data[:, 2]
    diemBc = in_data[:, 3]

    plt.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
    plt.plot(range(len(diemBc)), diemBc, 'g-', label="Diem B+")
    plt.xlabel('Lop')
    plt.ylabel('So sv dat diem')
    plt.legend(loc='upper right')
    plt.title(f"Scores for {'All Classes' if selected_class == 'All' else selected_class}")
    plt.show()

# Function to save filtered data
def save_filtered_data():
    if df is None:
        showinfo("Error", "Please load data first!")
        return

    selected_class = class_filter.get()
    filtered_df = df

    if selected_class != "All":
        filtered_df = df[df.iloc[:, 0] == selected_class]

    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if save_path:
        try:
            filtered_df.to_csv(save_path)
            showinfo("Success", "Filtered data saved successfully!")
        except Exception as e:
            showinfo("Error", f"Failed to save data: {e}")

# Main GUI application
def main():
    global class_filter, df
    df = None

    root = Tk()
    root.title("Student Scores GUI")
    root.geometry("400x300")

    Label(root, text="Student Scores Data Visualization", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Load Data", command=load_data, width=20).pack(pady=5)

    Label(root, text="Filter by Class:").pack(pady=5)
    class_filter = ttk.Combobox(root, state="readonly", width=30)
    class_filter.pack(pady=5)

    Button(root, text="Plot Data", command=plot_data, width=20).pack(pady=5)

    Button(root, text="Save Filtered Data", command=save_filtered_data, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
