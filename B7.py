import numpy as np
from tkinter import Tk, Label, Button, Text, END
from tkinter.messagebox import showinfo

# Function to process two matrices and display results
def process_matrices():
    try:
        # Get input matrices from user
        matrix_a_input = matrix_a_entry.get("1.0", END).strip()
        matrix_b_input = matrix_b_entry.get("1.0", END).strip()

        # Convert input strings to NumPy arrays
        matrix_a = np.array(eval(matrix_a_input))
        matrix_b = np.array(eval(matrix_b_input))

        # Perform operations
        sum_result = matrix_a + matrix_b
        elementwise_product = matrix_a * matrix_b
        matrix_product = np.dot(matrix_a, matrix_b)

        # Display results
        result_text.delete("1.0", END)
        result_text.insert(END, f"Matrix A + Matrix B:\n{sum_result}\n\n")
        result_text.insert(END, f"Elementwise Multiplication:\n{elementwise_product}\n\n")
        result_text.insert(END, f"Matrix Multiplication (Dot Product):\n{matrix_product}\n")

    except Exception as e:
        showinfo("Error", f"Invalid input or incompatible matrices: {e}")

# Main GUI application
def main():
    global matrix_a_entry, matrix_b_entry, result_text

    root = Tk()
    root.title("Matrix Operations GUI")
    root.geometry("600x600")

    Label(root, text="Enter Matrix A (e.g., [[1,2],[3,4]]):", font=("Arial", 12)).pack(pady=5)
    matrix_a_entry = Text(root, height=5, width=60)
    matrix_a_entry.pack(pady=5)

    Label(root, text="Enter Matrix B (e.g., [[4,3],[2,1]]):", font=("Arial", 12)).pack(pady=5)
    matrix_b_entry = Text(root, height=5, width=60)
    matrix_b_entry.pack(pady=5)

    Button(root, text="Process Matrices", command=process_matrices, width=20).pack(pady=10)

    Label(root, text="Results:", font=("Arial", 12)).pack(pady=5)
    result_text = Text(root, height=15, width=60)
    result_text.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()