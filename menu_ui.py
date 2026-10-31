import vn

import tkinter as tk
from tkinter import ttk
from pathlib import Path

global gui

gui = tk.Tk()
gui.title("HIMAPHAN RUNTIME")
gui.geometry("1920x1080")
gui.update()
gui.resizable(False,False)

BASE_DIR = Path(__file__).parent

def playGame(): #กดเริ่ม
    mainFrame.pack_forget()
    vn.start(gui)

def howToPlay(): #วิธีเล่น
    mainFrame.pack_forget()
    tutorialFrame.pack(fill="both", expand=True)

def close(): #ปิดเกม
    gui.destroy()

def menu(): #กลับหน้าแรก
    tutorialFrame.pack_forget()
    mainFrame.pack(fill="both", expand=True)

mainFrame=tk.Frame(gui, bg="#ffffff")
mainFrame.pack(fill="both", expand= True)

photo = tk.PhotoImage(file=BASE_DIR/"gold.png")
logo=ttk.Label(mainFrame, image=photo, compound = tk.TOP,).pack(expand=True)
tk.Label(mainFrame, text="เมื่อวัฏสงสารติด loop ... มีเพียงท่านที่สามารถแก้ไข",font=(("SOV_yamaka"), 50)).pack()
tk.Label(mainFrame, text="────────── ❖ ──────────",font=(("SOV_yamaka"), 50)).pack()
tk.Button(mainFrame, text="เริ่มเกม", font=(("SOV_yamaka"),50), command=playGame).pack(expand=True)
tk.Button(mainFrame, text="วิธีเล่น", font=(("SOV_yamaka"),50), command=howToPlay).pack(expand=True)
tk.Button(mainFrame, text="ออกเกม", font=(("SOV_yamaka"),50), command=close).pack(expand=True)



tutorialFrame = tk.Frame(gui, width=1920, height=1080)

tut_img = tk.PhotoImage(file=BASE_DIR / "tutorial.png")
tk.Label(tutorialFrame, image=tut_img).place(x=0, y=0, width=1920, height=1080)

tk.Button(tutorialFrame, text="กลับสู่เมนู", font=(("SOV_yamaka"), 30), command=menu).place(x=1650, y=980, width=220, height=60)


gui.mainloop()