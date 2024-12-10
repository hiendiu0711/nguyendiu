import numpy as np
from tkinter import Tk, Label, Button, Entry, Text, END
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt

# Function to process array and display results
def process_array():
    try:
        array_input = array_entry.get("1.0", END).strip()
        array = np.array(eval(array_input))

        largest = array.max()
        row_max = array.max(axis=1)
        col_min = array.min(axis=0)
        total_sum = array.sum()
        cumulative_sum = array.cumsum(axis=1)

        result_text.delete("1.0", END)
        result_text.insert(END, f"Largest element: {largest}\n")
        result_text.insert(END, f"Row-wise max: {row_max}\n")
        result_text.insert(END, f"Column-wise min: {col_min}\n")
        result_text.insert(END, f"Total sum: {total_sum}\n")
        result_text.insert(END, f"Cumulative sum along rows:\n{cumulative_sum}\n")

        # Plot the cumulative sum for visualization
        for i, row in enumerate(cumulative_sum):
            plt.plot(row, label=f"Row {i+1}")

        plt.title("Cumulative Sum Along Rows")
        plt.xlabel("Column Index")
        plt.ylabel("Cumulative Sum")
        plt.legend()
        plt.show()

    except Exception as e:
        showinfo("Error", f"Invalid input: {e}")

# Main GUI application
def main():
    global array_entry, result_text

    root = Tk()
    root.title("Array Processing GUI")
    root.geometry("500x500")

    Label(root, text="Enter a 2D Array (e.g., [[1,2,3],[4,5,6]]):", font=("Arial", 12)).pack(pady=10)

    array_entry = Text(root, height=5, width=50)
    array_entry.pack(pady=5)

    Button(root, text="Process Array", command=process_array, width=20).pack(pady=10)

    Label(root, text="Results:", font=("Arial", 12)).pack(pady=5)

    result_text = Text(root, height=15, width=50)
    result_text.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
