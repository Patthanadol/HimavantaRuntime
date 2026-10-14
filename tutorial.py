import tkinter as tk
from pathlib import Path

BASE_DIR = Path(__file__).parent

root = tk.Tk()
root.geometry("190x1080")

# 1. สร้างภาพพื้นหลัง (วางก่อน = อยู่เลเยอร์ล่างสุด)
bg_img = tk.PhotoImage(file=BASE_DIR / "gold.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.image = bg_img
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 2. นำ Widget อื่นๆ มาวางทับด้วย .place() (สร้างทีหลัง = ลอยทับด้านบน)
# ตัวอย่าง: กล่องข้อความบทสนทนา
dialogue_frame = tk.Frame(root, bg="#111116", bd=2, relief="solid")
dialogue_frame.place(x=60, y=780, width=1800, height=220)

# ข้อความข้างในกล่อง
text_label = tk.Label(
    dialogue_frame, 
    text="นี่คือข้อความที่วางทับบนพื้นหลัง...", 
    font=("MN KHUNYING", 22), 
    bg="#111116", 
    fg="white"
)
text_label.pack(padx=20, pady=20, anchor="w")

# ตัวอย่าง: ปุ่มกดลอยทับฉาก
btn = tk.Button(
    root, 
    text="โจมตี / Attack", 
    font=("MN KHUNYING", 20), 
    bg="#2f2e0a", 
    fg="white", 
    padx=20, 
    pady=10
)
btn.place(x=1550, y=700)

root.mainloop()