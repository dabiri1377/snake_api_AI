import time

from main_api import SnakeGame

test = SnakeGame(32)
print("test0")
test.start_game()
# while test.done():
#    time.sleep(0.2)
#   test.move_snake('down')
for _ in range(10):
    time.sleep(0.2)
    test.move_snake('down')

for _ in range(10):
    time.sleep(0.2)
    test.move_snake('left')

for _ in range(5):
    time.sleep(0.2)
    test.move_snake('up')

for _ in range(5):
    time.sleep(0.2)
    test.move_snake('right')