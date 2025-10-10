from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Khởi tạo đường dẫn rỗng
file_path = ""

def click():
    global file_path
    # Mở hộp thoại để chọn file ảnh
    file_path = filedialog.askopenfilename(
        title="Chọn file ảnh",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"), ("All files", "*.*")]
    )
    if file_path:  # Nếu người dùng chọn file
        # Dùng Pillow để mở hình ảnh
        pil_image = Image.open(file_path)
        
        # Chuyển đổi thành định dạng Tkinter
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # Hiển thị hình ảnh vào frame chính
        label.config(image=tk_image, text="")  # Xóa text khi có ảnh
        label.image = tk_image  # Lưu tham chiếu để tránh bị xóa bộ nhớ

def decompress():
    global file_path
    if file_path == "":
        label2 = Label(windown, text="Lỗi chưa có ảnh để giải nén", fg='red')
        label2.grid(row=2, column=0, columnspan=2)
    else:
        # Đọc ảnh và xử lý bằng NumPy và KMeans
        img = plt.imread(file_path)
        width, height, _ = img.shape
        img = img.reshape(width * height, 3)

        # Áp dụng KMeans
        kmeans = KMeans(n_clusters=3).fit(img)
        labels = kmeans.predict(img)
        clusters = kmeans.cluster_centers_

        # Tạo bức ảnh mới
        img2 = np.zeros_like(img)
        for i in range(len(img2)):
            img2[i] = clusters[labels[i]]
        img2 = img2.reshape(width, height, 3).astype(np.uint8)  # Đảm bảo định dạng uint8

        # Chuyển mảng NumPy thành ảnh PIL
        pil_image = Image.fromarray(img2)

        # Chuyển đổi thành định dạng Tkinter
        tk_image = ImageTk.PhotoImage(pil_image)

        # Hiển thị ảnh giải nén trong frame1
        label1.config(image=tk_image, text="")  # Xóa text khi có ảnh
        label1.image = tk_image  # Lưu tham chiếu để tránh bị xóa bộ nhớ
# Tạo cửa sổ Tkinter
windown = Tk()
windown.title("Xử lí hình ảnh")
windown.geometry("1200x600")  # Tăng kích thước cửa sổ

# Căn giữa toàn bộ nội dung
windown.grid_rowconfigure(0, weight=1)  # Dòng 0 được ưu tiên co giãn
windown.grid_rowconfigure(1, weight=0)  # Dòng nút không co giãn
windown.grid_columnconfigure(0, weight=1)  # Cột bên trái co giãn
windown.grid_columnconfigure(1, weight=1)  # Cột bên phải co giãn

# Tạo khung thứ nhất để hiển thị ảnh chính
frame = Frame(windown, width=513, height=400, bg="lightgray", relief=RIDGE, bd=2)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Tạo khung thứ hai để hiển thị ảnh "giải nén"
frame1 = Frame(windown, width=513, height=400, bg="lightgray", relief=RIDGE, bd=2)
frame1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Label trong khung hiển thị ảnh chính
label = Label(frame, text="Chưa chọn ảnh", bg="lightgray", fg="black")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label trong khung hiển thị ảnh đã giải nén
label1 = Label(frame1, text="Chưa có ảnh giải nén", bg="lightgray", fg="black")
label1.place(relx=0.5, rely=0.5, anchor=CENTER)

# Nút chọn file
btn = Button(
    windown,
    text="Ấn chọn ảnh",
    command=click,
    width=5,
    height=1,
    padx=50,
    pady=5,
    font=("Arial", 16)
)
btn.grid(row=1, column=0)

# Nút giải nén ảnh
btn = Button(
    windown,
    text="Giải nén ảnh",
    command=decompress,
    width=5,
    height=1,
    padx=50,
    pady=5,
    font=("Arial", 16)
)
btn.grid(row=1, column=1)

windown.mainloop()
