import random, sys, time
#start text
line = "=" * 40
spc = " " * 40
p_hp = 20
m_hp = 20
attacks = ["BONK", "SWIPE", "BOOM"]
def is_positive(int):
    if int <= 0:
        return 0
    elif int > 0:
        return int 
dmg = [2, 3, 5]
m_health = "===================="
p_health = "===================="
p_spc = ""
m_spc = ""
def dead(a):
    if a <= 0:
        return True
    else:
        return False
def damager(a,b):
    return a[:-b]
turn = 0
trn = 0
ag = 0
trn_num_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
print(f"{"\033[F\033[K" * 20}Welcome to Monster Fighter!")
print(line)
print(f"Attacks:{" " * 40}")
print("Bonk.....2dmg\nSwipe....3dmg\nBoom.....5dmg")
print(line)
while m_hp > 0 or p_hp > 0:
    trn_num = trn_num_list[trn]
    wt = 0
    while turn == 0:
            if ag == 0:
                pmv = input(f"What is your {trn_num} attack?  ").upper()
                if pmv in attacks:
                    pmv_i = attacks.index(pmv)
                    turn = 1
                else:
                    print("What was that?")
                    wt = 1
            elif ag == 1:
                pmv = input(f"{"\033[F\033[K" * 8}What is your {trn_num} attack?  ").upper()
                if pmv in attacks:
                    pmv_i = attacks.index(pmv)
                    turn = 1
                    ag = 0
                else:
                    print("What was that?")
                    wt = 1
    if m_hp > 0:
        m_health = damager(m_health,dmg[pmv_i])
        m_hp = m_hp - dmg[pmv_i]
    else:
        m_health = ""
        m_hp = 0
    if trn == 0:
        if wt == 0:
            print(f"\033[FPlayer used: {pmv}{spc}")
        else:
            print(f"{"\033[F\033[K" * 3}Player used: {pmv}{spc}")
    elif trn > 0:
        if wt == 0:
            print(f"{"\033[F\033[K" * 7}Player used: {pmv}{spc}")
        else:
            print(f"{"\033[F\033[K" * 9}Player used: {pmv}{spc}")
    mmv_i = random.randint(0, 2)
    print(f"Monster used: {attacks[mmv_i]}")
    print(line)
    p_hp = p_hp - dmg[mmv_i]
    if p_hp > 0:
        p_health = damager(p_health,dmg[mmv_i])
    else:
        p_health = ""
    p_spc = (p_spc + (" " * (dmg[mmv_i])))[:20]
    m_spc = (m_spc + (" " * (dmg[pmv_i])))[:20]
    print(f"Monster HP:|{m_health}{m_spc}|")
    print(f" Player HP:|{p_health}{p_spc}|")
    print(line)
    if dead(m_hp) == False and dead(p_hp) == True:
        print("GAME OVER")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print(line)
            print("Farewell")
            print(line)
            break
        else:
            turn = 0
            trn = 0
            p_hp = 20
            m_hp = 20
            ag = 1
            m_health = "===================="
            p_health = "===================="
            p_spc = ""
            m_spc = ""
    elif dead(m_hp) == True and dead(p_hp) == False:
        print("YOU WON!")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print(line)
            print("Farewell")
            print(line)
            break
        else:
            turn = 0
            trn = 0
            p_hp = 20
            m_hp = 20
            ag = 1
            m_health = "===================="
            p_health = "===================="
            p_spc = ""
            m_spc = ""
    elif dead(m_hp) == True and dead(p_hp) == True:
        print(f"A life for a life I guess.\n{line}\nGAME OVER")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print(line)
            print("Farewell")
            print(line)
            break
        else:
            turn = 0
            trn = 0
            p_hp = 10
            m_hp = 10
            ag = 1
            m_health = "=========="
            p_health = "=========="
            p_spc = ""
            m_spc = ""

    else:   
        turn = 0
        trn = trn + 1
        wt = 0