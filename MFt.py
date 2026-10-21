import time, sys

# Using carriage return
print("This is the first line.")
print("This is the first line.")
print("This is the first line.")
time.sleep(1)
# Using ANSI escape sequence to move up one line
print("\033[F\033[F\033[FThis is the second line.")
print("This is the second line")
print("This is the second line")
```