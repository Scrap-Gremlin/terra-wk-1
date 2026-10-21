import random, sys, time
#start text
line = "=" * 30
p_hp = 20
m_hp = 20
attacks = ["BONK", "SWIPE"]
dmg = [3, 5]
health_l = ["          ", "=         ", "==        ", "===       ", "====      ", "=====     ", "======    ", "=======   ", "========  ", "========= ", "=========="]
def dead(a):
    if a <= 0:
        return True
    else:
        return False
turn = 0
trn = 0
if isinstance((m_hp / 2), float):
    m_health = round((m_hp / 2))
else:
    m_health = m_hp / 2
m_health = health_l[m_health]
if isinstance((p_hp / 2), float):
    p_health = round((p_hp / 2))
else:
    p_health = p_hp / 2
p_health = health_l[p_health]
trn_num_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
print("Welcome to Monster Fighter!")
print(line)
print("Attacks:")
print("Bonk.....3dmg\nSwipe....5dmg")
print(line)
while m_hp > 0 or p_hp > 0:
    trn_num = trn_num_list[trn]
    while turn == 0:
            pmv = input(f"What is your {trn_num} attack?  ").upper()
            if pmv in attacks:
                pmv_i = attacks.index(pmv)
                turn = 1
            else:
                print("What was that?")
    m_hp = m_hp - dmg[pmv_i]
    if isinstance((m_hp / 2), float):
        m_health = round((m_hp / 2))
    else:
        m_health = m_hp / 2
    m_health = health_l[m_health]
    print(line)
    print(f" Player used:{pmv}")
    mmv_i = random.randint(0, 1)
    print(f"Monster used:{attacks[mmv_i]}")
    p_hp = p_hp - dmg[mmv_i]
    if isinstance((p_hp / 2), float):
        p_health = round((p_hp / 2))
    else:
        p_health = p_hp / 2
    p_health = health_l[p_health]
    print(line)
    print(f"Monster HP:{m_health}")
    print(f" Player HP:{p_health}")
    print(line)
    if dead(m_hp) == False and dead(p_hp) == True:
        print("GAME OVER")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print("Farewell")
            break
        else:
            print(line)
            turn = 0
            trn = 0
            p_hp = 20
            m_hp = 20
    elif dead(m_hp) == True and dead(p_hp) == False:
        print("YOU WON!")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print("Farewell")
            break
        else:
            print(line)
            turn = 0
            trn = 0
            p_hp = 20
            m_hp = 20
    elif dead(m_hp) == True and dead(p_hp) == True:
        print(f"A life for a life a guess.\n{line}\nGAME OVER")
        again = input("Play again? (y/n) ").lower()
        if "n" in again:
            print("Farewell")
            break
        else:
            print(line)
            turn = 0
            trn = 0
            p_hp = 20
            m_hp = 20

    else:
        print(line)
        turn = 0
        trn = trn + 1