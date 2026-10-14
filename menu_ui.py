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
tut = BASE_DIR /'tutorial1.png'

def playGame(): #กดเริ่ม
    mainFrame.pack_forget()
    vn.start(gui)

def howToPlay(): #วิธีเล่น
    mainFrame.pack_forget()
    tutorialFrame1.pack(fill="both", expand=True)

def htp2(): 
    tutorialFrame1.pack_forget()
    tutorialFrame2.pack(fill="both", expand=True)

def close(): #ปิดเกม
    gui.destroy()

def menu(): #กลับหน้าแรก
    tutorialFrame1.pack_forget()
    tutorialFrame2.pack_forget()
    mainFrame.pack(fill="both", expand=True)

mainFrame=tk.Frame(gui, bg="#ffffff")
mainFrame.pack(fill="both", expand= True)

photo = tk.PhotoImage(file=BASE_DIR/"gold.png")
logo=ttk.Label(mainFrame, image=photo, compound = tk.TOP,).pack(expand=True)
tk.Label(mainFrame, text="เมื่อวัฏสงสารติด loop ... มีเพียงท่านที่สามารถแก้ไข",font=(("SOV_yamaka"), 50)).pack()
tk.Label(mainFrame, text="────────── ❖ ──────────",font=(("SOV_yamaka"), 50)).pack()
tk.Button(mainFrame, text="เริ่มเกม", font=(("SOV_yamaka"),50), command=playGame).pack(expand=True)
tk.Button(mainFrame, text="วิธีเล่น", font=(("SOV_yamaka"),50), command=playGame).pack(expand=True)
tk.Button(mainFrame, text="ออกเกม", font=(("SOV_yamaka"),50), command=close).pack(expand=True)

#tutorial page 1
tutorialFrame1=tk.Frame(gui, bg="#2f2e0a")

tk.Label(tutorialFrame1, text="ภารกิจของเจ้า",font=(("SOV_yamaka"), 70), bg="#2f2e0a", fg="white").pack()
attack=tk.Label(tutorialFrame1, text="Attack", font=(("MN KHUNYING"), 50), bg="#f8f8ef", fg="white").place(x=50, y=100)
attack=tk.Label(tutorialFrame1, text="Ultimate", font=(("MN KHUNYING"), 50), bg="#f8f8ef", fg="white").place(x=1000, y=100)
attack=tk.Label(tutorialFrame1, text="Heal", font=(("MN KHUNYING"), 50), bg="#f8f8ef", fg="white").place(x=1500, y=100)


tk.Button(tutorialFrame1, text="next", font=(("SOV_yamaka"),20), command=htp2).pack()
tk.Button(tutorialFrame1, text="กลับสู่เมนู", font=(("SOV_yamaka"),20), command=menu).pack()


tutorialFrame2=tk.Frame(gui, bg="#d6d034")


gui.mainloop()