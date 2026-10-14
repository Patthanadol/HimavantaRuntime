import tkinter as tk

def battle(gui):
    battle = tk.Frame(gui, bg="green")
    battle.place(x=0, y=0, relwidth=1, relheight=1)

    bossHP = tk.Label(battle, text="█"*10, bg="yellow")
    bossHP.place(x=100, y=100, width=970, height=140)

    playerImg = tk.Frame(battle, bg="yellow")
    playerImg.place(x=100, y=290, width=460, height=690)

    PlayerHP = tk.Frame(battle, bg="yellow")
    PlayerHP.place(x=610, y=398, width=460, height=158)

    PlayerMana = tk.Frame(battle, bg="yellow")
    PlayerMana.place(x=610, y=714, width=460, height=158)

    bossImg = tk.Frame(battle, bg="yellow")
    bossImg.place(x=1120, y=100, width=700, height=630)

    attack = tk.Button(battle, text="⚔️\nโจมตี", font=(("SOV_yamaka"), 30), highlightthickness=0,bd=0)
    attack.place(x=1120, y=780, width=200, height=200)

    ulti = tk.Button(battle, text="✨\nมหาเวทย์", font=(("SOV_yamaka"), 30), highlightthickness=0,bd=0)
    ulti.place(x=1370, y=780, width=200, height=200)

    heal = tk.Button(battle, text="❤️‍🩹\nฟื้นฟู", font=(("SOV_yamaka"), 30), highlightthickness=0,bd=0)
    heal.place(x=1620, y=780, width=200, height=200)