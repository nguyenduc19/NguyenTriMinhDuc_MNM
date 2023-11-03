import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm xử lý tăng cường ánh sáng ảnh
def enhance_brightness():
    # Mở hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename()

    # Đọc ảnh từ tệp
    image = cv2.imread(file_path)

    if image is not None:
        # Tăng cường ánh sáng bằng cách thay đổi độ sáng và độ tương phản
        alpha = 1.5  # Độ sáng (có thể điều chỉnh)
        beta = 50   # Độ tương phản (có thể điều chỉnh)
        enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

        # Chuyển ảnh OpenCV sang định dạng PIL để hiển thị trong giao diện
        enhanced_image = Image.fromarray(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
        enhanced_image = ImageTk.PhotoImage(enhanced_image)

        # Hiển thị ảnh tăng cường ánh sáng trong giao diện
        label.config(image=enhanced_image)
        label.image = enhanced_image

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tăng cường ánh sáng ảnh")
root.geometry('500x500')

# Tạo nút để chọn ảnh và tăng cường ánh sáng
select_button = tk.Button(root, text="Chọn ảnh và tăng cường ánh sáng", command=enhance_brightness)
select_button.pack(pady=10)

# Tạo một nhãn để hiển thị ảnh tăng cường ánh sáng
label = tk.Label(root)
label.pack()

# Khởi chạy giao diện
root.mainloop()
