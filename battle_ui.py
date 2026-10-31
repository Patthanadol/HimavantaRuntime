import tkinter as tk
from pathlib import Path
import __main__
import player
import boss

BASE_DIR = Path(__file__).parent


def battle(gui):
    global battle_frame, boss_hp_text, player_hp_text, player_mana_text
    global player_attack_text, boss_attack_text, boss_img_label, player_img

    battle_frame = tk.Frame(gui, bg="black")
    battle_frame.place(x=0, y=0, relwidth=1, relheight=1)

    boss_hp_text = tk.StringVar()
    player_hp_text = tk.StringVar()
    player_mana_text = tk.StringVar()
    player_attack_text = tk.StringVar()
    boss_attack_text = tk.StringVar()

    player_img = tk.PhotoImage(file=BASE_DIR / "player.png")
    tk.Label(battle_frame, image=player_img).place(x=100, y=290, width=460, height=490)

    boss_img_label = tk.Label(battle_frame, bg="white")
    boss_img_label.place(x=1120, y=100, width=700, height=630)

    tk.Label(battle_frame, textvariable=boss_hp_text, font=("SOV_yamaka", 100), bg="#740000", fg="white").place(x=100, y=100, width=970, height=140)
    tk.Label(battle_frame, textvariable=player_hp_text, font=("SOV_yamaka", 50), bg="#177400", fg="white").place(x=610, y=290, width=460, height=200)
    tk.Label(battle_frame, textvariable=player_mana_text, font=("SOV_yamaka", 50), bg="#ddba00", fg="black").place(x=610, y=580, width=460, height=200)
    tk.Label(battle_frame, textvariable=player_attack_text, font=("SOV_yamaka", 30), bg="black", fg="white").place(x=100, y=830, width=460, height=150)
    tk.Label(battle_frame, textvariable=boss_attack_text, font=("SOV_yamaka", 30), bg="black", fg="#ddba00").place(x=610, y=830, width=460, height=150)

    tk.Button(battle_frame, text="⚔️\nโจมตี", font=("SOV_yamaka", 30), command=lambda: do_action("att"), highlightthickness=0, bd=0).place(x=1120, y=780, width=200, height=200)
    tk.Button(battle_frame, text="✨\nมหาเวทย์", font=("SOV_yamaka", 30), command=lambda: do_action("ult"), highlightthickness=0, bd=0).place(x=1370, y=780, width=200, height=200)
    tk.Button(battle_frame, text="❤️‍🩹\nฟื้นฟู", font=("SOV_yamaka", 30), command=lambda: do_action("heal"), highlightthickness=0, bd=0).place(x=1620, y=780, width=200, height=200)

    start_or_reset()


def refresh_ui():
    global boss_img
    player_hp_text.set(f"{player.name} : {player.get_stat('hp')} โลหิต")
    player_mana_text.set(f"{player.name} : {player.get_stat('mana')} เวทย์")

    if boss.state == "win":
        boss_hp_text.set("เจ้ามีชัย!")
    elif boss.state == "lose":
        boss_hp_text.set("เจ้าพ่าย!")
    else:
        name, _, _, _, img_file = boss.get_boss()
        boss_hp_text.set(f"{name} : {boss.boss_hp} โลหิต")
        boss_img = tk.PhotoImage(file=BASE_DIR / img_file)
        boss_img_label["image"] = boss_img

def start_or_reset(alert=None):
    if alert:
        alert.destroy()
    boss.new_game()
    player_attack_text.set("จงเลือกทักษะแห่งเจ้า")
    boss_attack_text.set("")
    refresh_ui()


def do_action(mode):
    if boss.state != "play":
        return

    dmg = 0
    if mode == "att":
        dmg = player.att()
    elif mode == "ult":
        dmg = player.ult()
        if dmg is None:
            return show_alert("MANA", "เวทย์ไม่เพียงพอ!")
    elif mode == "heal":
        if player.get_stat("hp") >= player.get_stat("maxhp"):
            return show_alert("HEAL", "โลหิตเต็มอยู่แล้ว!")
        if not player.heal():
            return show_alert("MANA", "เวทย์ไม่เพียงพอ!")

    event, boss_dmg, msg = boss.process_turn(dmg)
    player_attack_text.set("เจ้าฟื้นฟูพลังชีวิต" if mode == "heal" else f"เจ้าสร้างความเสียหาย {dmg} โลหิต")
    boss_attack_text.set(f"ศัตรูสร้างความเสียหาย {boss_dmg} โลหิต")
    refresh_ui()

    if event in ("เจ้ามีชัย!", "เจ้าพ่าย!", "ยินดีด้วย"):
        show_alert(event, msg, restart=(event == "เจ้าพ่าย!"))


def show_alert(title, message, restart=False):
    alert = tk.Toplevel(battle_frame)
    alert.title(title)
    alert.geometry("700x300+610+390")
    alert.resizable(False, False)

    tk.Label(alert, text=message, font=("MN KHUNYING", 35)).pack(pady=35)
    btn_text = "เริ่มเล่นใหม่" if restart else "ตกลง"

    if restart:
        cmd = lambda: start_or_reset(alert)
    elif boss.state == "win":
        cmd = lambda: (battle_frame.destroy(), __main__.menu())
    else:
        cmd = alert.destroy

    tk.Button(alert, text=btn_text, font=("MN KHUNYING", 25), command=cmd).pack()