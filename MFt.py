# libraries
import sys, time, random
# lists
attacks = ["BONK", "SWIPE", "BOOM", "(turn skipped)", "  Use a move!"]
trn_num_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
dmg = [2, 3, 5, 0]
# filler variables
line = "=" * 40
spc = " " * 40
p_spc = ""
m_spc = ""
# health variables
p_hp_val = 20
m_hp_val = 20
m_hp_bar = "===================="
p_hp_bar = "===================="
p_dmg = 0
m_dmg = 0
# move selection variables
turn_done = False
trn = 0
ag = False
retry = False
trn_num = trn_num_list[trn]
# limiting variables
p_skip = False
m_skip = False
wait = False
p_limit_swipe = 0
m_limit_swipe = 0
# functions
def dead(a):
    if a <= 0:
        return True
    else:
        return False
def damager(a,b):
    if b <= 0:
        return a
    elif b > 0:
        return a[:-b]
# start
while m_hp_val >= 0 or p_hp_val >= 0:
    print(f"{"\033[F\033[K" * 30}Welcome to Monster Fighter!")
    print(line)
    print(f"Attacks:{spc}")
    print("Bonk.....2dmg\nSwipe....3dmg\nBoom.....5dmg")
    print(line)
    print(f" Player used:{attacks[4]}")
    print(f"Monster used:{attacks[4]}")
    print(line)
    print(f" Player HP:|{p_hp_bar}{p_spc}|")
    print(f"Monster HP:|{m_hp_bar}{m_spc}|")
    print(line)
    if p_skip == False:
        while turn_done == False:
            if retry == False:
                pmv = input(f"What is your {trn_num} attack?  ").upper()
            elif retry == True:
                pmv = input(f"{"\033[F\033[K" * 2}What is your {trn_num} attack?  ").upper()
            if pmv in attacks:
                p_dmg = dmg[attacks.index(pmv)]
                p_hp_val = p_hp_val - p_dmg
                p_hp_bar = p_hp_bar[:-p_dmg]
                p_spc = p_spc + (" " * (p_dmg))
                retry = False
                turn_done = True
            elif pmv not in attacks:
                print("You can't do that.")
                time.sleep(1.3)
                retry = True
    elif p_skip == True:
        print("You need to recharge, turn skipped.")
        wait = True

