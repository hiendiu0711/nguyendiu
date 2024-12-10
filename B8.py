from sympy import Symbol, diff, integrate, limit, solve, oo, sin, exp
from tkinter import Tk, Label, Button, Text, Entry, END, filedialog
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
import numpy as np

# Function to process the input expression
def process_expression():
    try:
        # Get input expression from user
        expression = expression_entry.get("1.0", END).strip()
        x = Symbol('x')

        # Perform symbolic computations
        derivative = diff(expression, x)
        indefinite_integral = integrate(expression, x)
        definite_integral = integrate(sin(x**2), (x, -oo, oo))
        limit_result = limit(sin(x) / x, x, 0)
        roots = solve(x**2 - 2, x)

        # Display results
        result_text.delete("1.0", END)
        result_text.insert(END, f"Expression: {expression}\n\n")
        result_text.insert(END, f"Derivative: {derivative}\n\n")
        result_text.insert(END, f"Indefinite Integral: {indefinite_integral}\n\n")
        result_text.insert(END, f"Definite Integral of sin(x^2) from -∞ to ∞: {definite_integral}\n\n")
        result_text.insert(END, f"Limit of sin(x)/x as x approaches 0: {limit_result}\n\n")
        result_text.insert(END, f"Roots of x^2 - 2: {roots}\n")

    except Exception as e:
        showinfo("Error", f"Invalid input or computation error: {e}")

# Function to plot the graph of the expression
def plot_expression():
    try:
        expression = expression_entry.get("1.0", END).strip()
        x = Symbol('x')
        expr = eval(expression.replace('^', '**'))  # Replace '^' with '**' for power operations

        # Generate values for plotting
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [float(expr.subs(x, val)) for val in x_vals]

        plt.plot(x_vals, y_vals, label=str(expression))
        plt.title("Graph of the Expression")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        showinfo("Error", f"Unable to plot expression: {e}")

# Function to evaluate the expression at a specific point
def evaluate_at_point():
    try:
        expression = expression_entry.get("1.0", END).strip()
        point = float(point_entry.get().strip())
        x = Symbol('x')
        expr = eval(expression.replace('^', '**'))  # Replace '^' with '**' for power operations
        value = float(expr.subs(x, point))
        showinfo("Evaluation Result", f"The value of the expression at x = {point} is {value}")
    except Exception as e:
        showinfo("Error", f"Unable to evaluate expression: {e}")

# Function to save results to a file
def save_results():
    try:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(result_text.get("1.0", END).strip())
            showinfo("Success", "Results saved successfully!")
    except Exception as e:
        showinfo("Error", f"Failed to save results: {e}")

# Main GUI application
def main():
    global expression_entry, result_text, point_entry

    root = Tk()
    root.title("Symbolic Computation GUI")
    root.geometry("600x700")

    Label(root, text="Enter a mathematical expression (in terms of x):", font=("Arial", 12)).pack(pady=5)

    expression_entry = Text(root, height=5, width=60)
    expression_entry.pack(pady=5)

    Button(root, text="Process Expression", command=process_expression, width=20).pack(pady=10)
    Button(root, text="Plot Expression", command=plot_expression, width=20).pack(pady=10)

    Label(root, text="Evaluate at a specific point (x):", font=("Arial", 12)).pack(pady=5)
    point_entry = Entry(root, width=30)
    point_entry.pack(pady=5)
    Button(root, text="Evaluate", command=evaluate_at_point, width=20).pack(pady=10)

    Button(root, text="Save Results", command=save_results, width=20).pack(pady=10)

    Label(root, text="Results:", font=("Arial", 12)).pack(pady=5)

    result_text = Text(root, height=20, width=60)
    result_text.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()