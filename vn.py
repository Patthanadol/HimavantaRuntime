import tkinter as tk
from pathlib import Path

import battle_ui

BASE_DIR = Path(__file__).parent

def start(gui):
    global namePage, nameEntry
    namePage = tk.Frame(gui, bd=0, highlightthickness=0)
    namePage.pack(fill="both", expand=True)

    nameLabel = tk.Label(namePage, text="ท่านมีนามว่าอันใดกัน", font=(("MN KHUNYING"), 80), anchor="s")
    nameLabel.pack(padx=100, pady=0, fill="both", expand=True,)

    nameEntry = tk.Entry(namePage, font=(("MN KHUNYING"), 50), justify="center")
    nameEntry.pack(padx=100, pady=0, anchor="center")
    nameEntry.focus()

    nameBTN=tk.Button(namePage,text="ต่อไป",font=(("SOV_yamaka"),30), command=lambda:next_page(gui))
    nameBTN.pack(padx=10, pady=10, expand=True, anchor="n")

def next_page(gui):
    global nameInput
    nameInput = nameEntry.get()
    if len(nameInput) > 10:
        alert=tk.Tk()
        alert.title("ERROR")
        alert.geometry("700x250+610+410")
        alert.resizable(False,False)
        tk.Label(alert, text="นามของท่านมิอาจเกิน 10 อักขระ!!", font=(("MN KHUNYING"), 40)).pack(pady=30)
        tk.Button(alert, text="ลองอีกสักครา", font=(("MN KHUNYING"), 30), command=alert.destroy).pack(anchor="s")
    elif len(nameInput) == 0:
        alert=tk.Tk()
        alert.title("ERROR")
        alert.geometry("700x250+610+410")
        alert.resizable(False,False)
        tk.Label(alert, text="ท่านมิได้รับอนุญาตให้นิรนาม", font=(("MN KHUNYING"), 40)).pack(pady=30)
        tk.Button(alert, text="ลองอีกสักครา", font=(("MN KHUNYING"), 30), command=alert.destroy).pack(anchor="s")
    else:
        namePage.pack_forget()
        visual(gui)



def vn1():
    page1.place_forget()
    bg_label.config(image=bg2)
    bg_label.image = bg2
    page2.place(x=50, y=780, width=1820, height=200)

def vn2():
    page2.place_forget()
    bg_label.config(image=bg3)
    bg_label.image = bg3
    page3.place(x=50, y=780, width=1820, height=200)


def vn3():
    page3.place_forget()
    bg_label.config(image=bg4)
    bg_label.image = bg4
    page4.place(x=50, y=780, width=1820, height=200)

def vn4():
    page4.place_forget()
    bg_label.config(image=bg3)
    bg_label.image = bg3
    page5.place(x=50, y=780, width=1820, height=200)

def vn5():
    page5.place_forget()
    bg_label.config(image=bg4)
    bg_label.image = bg4
    page6.place(x=50, y=780, width=1820, height=200)

def vn6():
    page6.place_forget()
    bg_label.config(image=bg3)
    bg_label.image = bg3
    page7.place(x=50, y=780, width=1820, height=200)

def vn7(gui):
    vnFrame.pack_forget()
    battle_ui.battle(gui)


def visual(gui):
    global page1, page2, page3, page4, page5, page6, page7
    global vnFrame, bg_label
    global bg2, bg3, bg4, bg5, bg6
    vnFrame = tk.Frame(gui, bd=0, highlightthickness=0)
    vnFrame.pack(fill="both", expand=True)

    bg = tk.PhotoImage(file=BASE_DIR / "bg.png")
    bg2 = tk.PhotoImage(file=BASE_DIR / "bg2.png")
    bg3 = tk.PhotoImage(file=BASE_DIR / "bg3.png")
    bg4 = tk.PhotoImage(file=BASE_DIR / "bg4.png")
    bg5 = tk.PhotoImage(file=BASE_DIR / "bg4.png")
    bg6 = tk.PhotoImage(file=BASE_DIR / "bg4.png")

    bg_label = tk.Label(vnFrame, image=bg)

    bg_label.image = bg #พื้นหลังหน้า vn
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    page1 = tk.LabelFrame(vnFrame, text=f" 🔱 ทวยเทพ 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    page1.place(x=50, y=780, width=1820, height=200)
    tk.Label(page1, text=f"ยินดีต้อนรับ ท่าน{nameInput} เบื้องหน้าท่าน คือ เขาพระสุเมรุ ศูนย์กลางจักรวาลที่สรรพสิ่งควรเวียนว่ายตามกฎแห่งกรรม...",
             font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page1,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn1,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")


    page2 = tk.LabelFrame(vnFrame, text=f" 🔱 ทวยเทพ 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0, bg="#2A2929", fg="white")
    tk.Label(page2, text=f"ทว่าบัดนี้ กาลเวลาเริ่มติดขัด ใบไม้หยุดร่วง สัตว์เทพเริ่มเสียการควบคุม",
                font=(("MN KHUNYING"), 30),justify="left",anchor="w", bg="#2A2929", fg="white").pack(fill="x")
    tk.Button(page2,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn2,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")


    page3 = tk.LabelFrame(vnFrame, text=f" 🔱 มหาฤๅษี 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    tk.Label(page3, text=f"{nameInput}... เจ้าสังเกตเห็นรอยแยกบนท้องฟ้านั่นหรือไม่?",
                    font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page3,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn3,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")


    page4 = tk.LabelFrame(vnFrame, text=f" 🔱 {nameInput} 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    tk.Label(page4, text=f"เห็นขอรับอาจารย์! เหมือนมีใครเอาหมึกดำมาขีดทับสวรรค์เลย!",
                    font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page4,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn4,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")


    page5 = tk.LabelFrame(vnFrame, text=f" 🔱 มหาฤๅษี 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    tk.Label(page5, text=f"นั่นคือ 'มิจฉาวาระ' จักรวาลกำลังผิดปกติ มีเพียงแค่เจ้าจะต้องปราบสัตว์พิทักษ์ที่คุ้มคลั่ง จักรวาลจึงจะกลับคืนดังเดิม",
                    font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page5,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn5,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")

    page6 = tk.LabelFrame(vnFrame, text=f" 🔱 {nameInput} 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    tk.Label(page6, text=f"แต่พวกเขามีพลังแข็งแกร่งมาก ข้าจะสู้ไหวหรือท่านอาจารย์",
                    font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page6,text="ต่อไป",font=(("SOV_yamaka"),20),command=vn6,highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")

    page7 = tk.LabelFrame(vnFrame, text=f" 🔱 มหาฤๅษี 🔱", font=(("SOV_yamaka"), 40), padx=30, pady=20, bd=0)
    tk.Label(page7, text=f"ข้าได้ประสาทพลังโจมตี มหาเวท และฟื้นฟูไว้ในกายเจ้าแล้ว... จงเชื่อมั่นในพลังแห่งดวงชะตาของเจ้า",
                    font=(("MN KHUNYING"), 30),justify="left",anchor="w").pack(fill="x")
    tk.Button(page7,text="ออกเดินทาง",font=(("SOV_yamaka"),20),command=lambda:vn7(gui),highlightthickness=0,bd=0).place(relx=0.98, rely=0.68, anchor="center")






