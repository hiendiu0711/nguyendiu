import cv2
import numpy as np
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image, ImageTk

# Hàm xử lý ảnh Sobel
def apply_sobel():
    global img, img_display
    sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    # Chuyển đổi sang dạng ảnh có thể hiển thị trong Tkinter
    sobel_horizontal = cv2.convertScaleAbs(sobel_horizontal)
    sobel_vertical = cv2.convertScaleAbs(sobel_vertical)
    img_display = Image.fromarray(sobel_horizontal)
    img_display = img_display.resize((1000, 1000))
    img_display = ImageTk.PhotoImage(img_display)
    label.config(image=img_display)
    messagebox.showinfo("Info", "Đã áp dụng bộ lọc Sobel!")

# Hàm áp dụng bộ lọc Gaussian
def apply_gaussian_blur():
    global img, img_display
    gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)
    img_display = Image.fromarray(gaussian_blur)
    img_display = img_display.resize((1000, 1000))
    img_display = ImageTk.PhotoImage(img_display)
    label.config(image=img_display)
    messagebox.showinfo("Info", "Đã áp dụng bộ lọc Gaussian!")

# Hàm điều chỉnh độ sáng ảnh
def adjust_brightness(factor):
    global img, img_display
    brightness_img = cv2.convertScaleAbs(img, alpha=factor, beta=0)
    img_display = Image.fromarray(brightness_img)
    img_display = img_display.resize((1000, 1000))
    img_display = ImageTk.PhotoImage(img_display)
    label.config(image=img_display)
    messagebox.showinfo("Info", "Đã điều chỉnh độ sáng ảnh!")

# Hàm chọn ảnh
def load_image():
    global img, img_display
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        img_display = Image.fromarray(img)
        img_display = img_display.resize((1000, 1000))
        img_display = ImageTk.PhotoImage(img_display)
        label.config(image=img_display)

# Khởi tạo cửa sổ chính của giao diện
root = Tk()
root.title("Chương trình xử lý ảnh")

# Thêm các nút chức năng vào giao diện
load_button = Button(root, text="Tải ảnh", command=load_image)
load_button.pack()

sobel_button = Button(root, text="Áp dụng Sobel", command=apply_sobel)
sobel_button.pack()

gaussian_button = Button(root, text="Áp dụng bộ lọc Gaussian", command=apply_gaussian_blur)
gaussian_button.pack()

brightness_button = Button(root, text="Tăng độ sáng", command=lambda: adjust_brightness(1.5))
brightness_button.pack()

# Hiển thị ảnh trong giao diện
label = Label(root)
label.pack()

root.mainloop()
