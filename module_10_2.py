import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        dur = 100
        i = 0
        while dur:
            dur = dur - self.power
            i += 1
            print(f'{self.name} сражается {i} дней(дня), осталось {dur} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {i} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
second_knight.join()
first_knight.join()
