import sys, time

for x in range(11):
    sys.stdout.write(f"\r{x}")
    sys.stdout.flush()
    time.sleep(1)