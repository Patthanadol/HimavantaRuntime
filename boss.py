import random
import player

healAfterBoss = 40

# [ชื่อบอส, HP สูงสุด, ดาเมจต่ำสุด, ดาเมจสูงสุด, ไฟล์รูป]
bosses = [
    ["พญาวิหค", 100, 3, 10, "b1.png"],
    ["พญาอานนท์", 160, 5, 14, "b2.png"],
    ["ฤาษี", 200, 7, 18, "b3.png"]
]

stage = 0
boss_hp = 100
state = "play"


def get_boss():
    return bosses[stage]


def new_game():
    global stage, boss_hp, state
    player.resetPlayer()
    stage = 0
    boss_hp = bosses[0][1]
    state = "play"


def process_turn(player_dmg):
    global stage, boss_hp, state
    if state != "play":
        return state, 0, ""

    boss_hp = max(0, boss_hp - player_dmg)

    if boss_hp == 0:
        old_name = bosses[stage][0]
        stage = stage+1
        if stage == len(bosses):
            state = "win"
            return "เจ้ามีชัย!", 0, "เจ้ามีชัย!\nคืนความสมดุลสู่โลกแล้ว"
        
        boss_hp = bosses[stage][1]
        new_hp = min(player.get_stat("hp") + healAfterBoss, player.get_stat("maxhp"))
        player.set_stat("hp", new_hp)
        return "ยินดีด้วย", 0, f"มีชัยแก่ {old_name} แล้ว!\nโลหิตของเจ้าฟื้นฟู {healAfterBoss} หน่วย"

    _, _, low, high, _ = bosses[stage]
    boss_dmg = random.randint(low, high)
    hp = max(0, player.get_stat("hp") - boss_dmg)
    player.set_stat("hp", hp)

    if hp == 0:
        state = "lose"
        return "เจ้าพ่าย!", boss_dmg, "เจ้าพ่าย!\nโลหิตของเจ้าสิ้นแล้ว"

    return "play", boss_dmg, ""