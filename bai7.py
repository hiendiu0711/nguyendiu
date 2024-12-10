import numpy as np
from tkinter import Tk, Label, Button, Text, END
from tkinter.messagebox import showinfo


# Function to get matrices from user input
def get_matrices():
    try:
        matrix_a_input = matrix_a_entry.get("1.0", END).strip()
        matrix_b_input = matrix_b_entry.get("1.0", END).strip()
        matrix_a = np.array(eval(matrix_a_input))
        matrix_b = np.array(eval(matrix_b_input))
        return matrix_a, matrix_b
    except Exception as e:
        showinfo("Error", f"Invalid input: {e}")
        return None, None


# Function to clear the result text box
def clear_results():
    result_text.delete("1.0", END)


# Individual functions for each operation
def calculate_sum():
    clear_results()  # Clear old results
    matrix_a, matrix_b = get_matrices()
    if matrix_a is not None and matrix_b is not None:
        try:
            result = matrix_a + matrix_b
            result_text.insert(END, f"Matrix A + Matrix B:\n{result}\n")
        except Exception as e:
            showinfo("Error", f"Cannot calculate sum: {e}")


def calculate_elementwise_product():
    clear_results()  # Clear old results
    matrix_a, matrix_b = get_matrices()
    if matrix_a is not None and matrix_b is not None:
        try:
            result = matrix_a * matrix_b
            result_text.insert(END, f"Elementwise Multiplication:\n{result}\n")
        except Exception as e:
            showinfo("Error", f"Cannot calculate elementwise product: {e}")


def calculate_matrix_product():
    clear_results()  # Clear old results
    matrix_a, matrix_b = get_matrices()
    if matrix_a is not None and matrix_b is not None:
        try:
            result = np.dot(matrix_a, matrix_b)
            result_text.insert(END, f"Matrix Multiplication (Dot Product):\n{result}\n")
        except Exception as e:
            showinfo("Error", f"Cannot calculate dot product: {e}")


def calculate_determinant():
    clear_results()  # Clear old results
    matrix_a, _ = get_matrices()
    if matrix_a is not None:
        try:
            result = np.linalg.det(matrix_a)
            result_text.insert(END, f"Determinant of Matrix A:\n{result:.2f}\n")
        except Exception as e:
            showinfo("Error", f"Cannot calculate determinant of A: {e}")


def calculate_inverse():
    clear_results()  # Clear old results
    matrix_a, _ = get_matrices()
    if matrix_a is not None:
        try:
            result = np.linalg.inv(matrix_a)
            result_text.insert(END, f"Inverse of Matrix A:\n{result}\n")
        except Exception as e:
            showinfo("Error", f"Cannot calculate inverse of A: {e}")


def calculate_transpose():
    clear_results()  # Clear old results
    matrix_a, matrix_b = get_matrices()
    if matrix_a is not None and matrix_b is not None:
        result_text.insert(END, f"Transpose of Matrix A:\n{matrix_a.T}\n")
        result_text.insert(END, f"Transpose of Matrix B:\n{matrix_b.T}\n")


# Main GUI application
def main():
    global matrix_a_entry, matrix_b_entry, result_text

    root = Tk()
    root.title("Enhanced Matrix Operations GUI")
    root.geometry("700x700")

    Label(root, text="Enter Matrix A (e.g., [[1,2],[3,4]]):", font=("Arial", 12)).pack(pady=5)
    matrix_a_entry = Text(root, height=5, width=60)
    matrix_a_entry.pack(pady=5)

    Label(root, text="Enter Matrix B (e.g., [[4,3],[2,1]]):", font=("Arial", 12)).pack(pady=5)
    matrix_b_entry = Text(root, height=5, width=60)
    matrix_b_entry.pack(pady=5)

    Button(root, text="Calculate Sum", command=calculate_sum, width=20).pack(pady=5)
    Button(root, text="Elementwise Multiplication", command=calculate_elementwise_product, width=25).pack(pady=5)
    Button(root, text="Matrix Multiplication", command=calculate_matrix_product, width=25).pack(pady=5)
    Button(root, text="Calculate Determinant (Matrix A)", command=calculate_determinant, width=30).pack(pady=5)
    Button(root, text="Calculate Inverse (Matrix A)", command=calculate_inverse, width=30).pack(pady=5)
    Button(root, text="Calculate Transpose", command=calculate_transpose, width=20).pack(pady=5)

    Button(root, text="Clear Results", command=clear_results, width=20).pack(pady=10)

    Label(root, text="Results:", font=("Arial", 12)).pack(pady=5)
    result_text = Text(root, height=15, width=60)
    result_text.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
