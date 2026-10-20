import sys, time
m_hp = 0
while True:
    time.sleep(1)
    m_hp_s = m_hp
    m_hp = m_hp + 1
    if m_hp > m_hp_s:   
        health_l = ["==========", "=========-", "========= ", "========- ", "========  ", "=======-  ", "=======   ", "======-   ", "======    ", "=====-    ", "=====     ", "====-     ", "====      ", "===-      ", "===       ", "==-       ", "==        ", "=-        ", "=         ", "-         ", "          "]
        health = health_l[m_hp]
        sys.stdout.write(f"\r{health}")
        sys.stdout.flush()