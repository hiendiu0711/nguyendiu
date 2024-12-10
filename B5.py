import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt

# Function to load and display the original image
def load_image():
    global img
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    try:
        if filepath:
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        else:
            img = cv2.imread('picl.png', cv2.IMREAD_GRAYSCALE)
        
        if img is not None:
            cv2.imshow("Original Image", img)
            showinfo("Success", "Image loaded successfully!")
        else:
            showinfo("Error", "Failed to load image. Ensure the file exists and is a valid image.")
    except Exception as e:
        showinfo("Error", f"Failed to load image: {e}")

# Function to resize image and display different sizes
def resize_and_display():
    if img is None:
        showinfo("Error", "Please load an image first!")
        return

    # Resizing the image
    half = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
    bigger = cv2.resize(img, (1050, 1610))
    stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_LINEAR)

    # Displaying the images using Matplotlib
    Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
    Images = [img, half, bigger, stretch_near]

    for i in range(len(Images)):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(Images[i], cmap='gray')

    plt.show()

# Function to save resized images
def save_resized_image():
    if img is None:
        showinfo("Error", "Please load an image first!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if save_path:
        try:
            # Resize the image to half-size for saving as an example
            half = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
            cv2.imwrite(save_path, half)
            showinfo("Success", "Resized image saved successfully!")
        except Exception as e:
            showinfo("Error", f"Failed to save resized image: {e}")

# Main GUI application
def main():
    global img
    img = None

    root = Tk()
    root.title("Image Resizing GUI")
    root.geometry("400x300")

    Label(root, text="Image Resizing Tool", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Load Image", command=load_image, width=20).pack(pady=5)
    Button(root, text="Resize and Display", command=resize_and_display, width=20).pack(pady=5)
    Button(root, text="Save Resized Image", command=save_resized_image, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ chính của Tkinter
    load_image("path/to/your/pic1.png")  # Đường dẫn tới ảnh mặc định
    root.mainloop()
