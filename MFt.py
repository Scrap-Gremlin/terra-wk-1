import sys, time

health = "=========="
for x in range(11):
    sys.stdout.write(f"\r\033[K{health}")
    sys.stdout.flush()
    health = health[:-2]
    time.sleep(.5)
