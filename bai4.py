import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Scale, HORIZONTAL
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk


class XuLyAnhXQuang:
    def __init__(self, root):
        self.root = root
        self.root.title("Xử Lý Ảnh X-Quang")
        self.root.geometry("600x500")

        self.img = None  # Ảnh gốc
        self.processed_img = None  # Ảnh đã qua xử lý

        # Tiêu đề
        Label(root, text="Công Cụ Xử Lý Ảnh X-Quang", font=("Arial", 16)).pack(pady=10)

        # Nút chọn ảnh
        Button(root, text="Chọn Ảnh X-Quang", command=self.load_image, width=20).pack(pady=5)

        # Hiển thị thanh điều chỉnh độ sắc nét
        Label(root, text="Điều Chỉnh Độ Sắc Nét:").pack(pady=5)
        self.kernel_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, length=300)
        self.kernel_slider.set(9)  # Giá trị mặc định
        self.kernel_slider.pack(pady=5)

        # Nút áp dụng bộ lọc
        Button(root, text="Áp Dụng Bộ Lọc", command=self.apply_filter, width=20).pack(pady=5)

        # Nút hiển thị histogram
        Button(root, text="Hiển Thị Biểu Đồ Histogram", command=self.show_histogram, width=30).pack(pady=5)

        # Nút lưu ảnh
        Button(root, text="Lưu Ảnh Đã Xử Lý", command=self.save_image, width=20).pack(pady=5)

        # Khung hiển thị ảnh
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

    def load_image(self):
        """Hàm chọn ảnh từ thư viện."""
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if filepath:
            try:
                self.img = cv2.imread(filepath)
                self.display_image(self.img)
                showinfo("Thành Công", "Ảnh X-Quang đã được tải thành công!")
            except Exception as e:
                showinfo("Lỗi", f"Tải ảnh thất bại: {e}")

    def apply_filter(self):
        """Áp dụng bộ lọc làm sắc nét."""
        if self.img is None:
            showinfo("Lỗi", "Vui lòng chọn ảnh X-Quang trước!")
            return

        kernel_strength = self.kernel_slider.get()
        kernel_sharpen = np.array([[-1, -1, -1], [-1, kernel_strength, -1], [-1, -1, -1]])
        self.processed_img = cv2.filter2D(self.img, -1, kernel_sharpen)

        self.display_image(self.processed_img)
        showinfo("Thành Công", f"Đã áp dụng bộ lọc với độ sắc nét {kernel_strength}!")

    def display_image(self, image):
        """Hiển thị ảnh trên giao diện."""
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def show_histogram(self):
        """Hiển thị histogram của ảnh."""
        if self.img is None:
            showinfo("Lỗi", "Vui lòng chọn ảnh X-Quang trước!")
            return

        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Biểu Đồ Histogram", gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self):
        """Lưu ảnh đã xử lý."""
        if self.processed_img is None:
            showinfo("Lỗi", "Vui lòng áp dụng bộ lọc trước!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if save_path:
            try:
                cv2.imwrite(save_path, self.processed_img)
                showinfo("Thành Công", "Ảnh đã được lưu thành công!")
            except Exception as e:
                showinfo("Lỗi", f"Lưu ảnh thất bại: {e}")


if __name__ == "__main__":
    root = Tk()
    app = XuLyAnhXQuang(root)
    root.mainloop()
