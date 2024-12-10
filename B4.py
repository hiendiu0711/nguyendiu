import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Scale, HORIZONTAL
from tkinter.messagebox import showinfo

# Function to load and display the original image
def load_image():
    global img
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        try:
            img = cv2.imread(filepath)
            cv2.imshow("Original", img)
            showinfo("Success", "Image loaded successfully!")
        except Exception as e:
            showinfo("Error", f"Failed to load image: {e}")

# Function to apply sharpening filters
def apply_filter():
    if img is None:
        showinfo("Error", "Please load an image first!")
        return

    kernel_strength = kernel_slider.get()

    kernel_sharpen = np.array([[-1, -1, -1], [-1, kernel_strength, -1], [-1, -1, -1]])
    output = cv2.filter2D(img, -1, kernel_sharpen)

    cv2.imshow(f"Sharpened Image (Strength {kernel_strength})", output)

# Function to save the processed image
def save_image():
    if img is None:
        showinfo("Error", "Please load an image first!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if save_path:
        try:
            kernel_strength = kernel_slider.get()
            kernel_sharpen = np.array([[-1, -1, -1], [-1, kernel_strength, -1], [-1, -1, -1]])
            output = cv2.filter2D(img, -1, kernel_sharpen)
            cv2.imwrite(save_path, output)
            showinfo("Success", "Image saved successfully!")
        except Exception as e:
            showinfo("Error", f"Failed to save image: {e}")

# Main GUI application
def main():
    global img, kernel_slider
    img = None

    root = Tk()
    root.title("Image Sharpening GUI")
    root.geometry("400x300")

    Label(root, text="Image Sharpening Tool", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Load Image", command=load_image, width=20).pack(pady=5)

    Label(root, text="Adjust Sharpening Strength:").pack(pady=5)
    kernel_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, length=300)
    kernel_slider.set(9)  # Default strength
    kernel_slider.pack(pady=5)

    Button(root, text="Apply Filter", command=apply_filter, width=20).pack(pady=5)
    Button(root, text="Save Image", command=save_image, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
