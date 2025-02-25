# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 18:59
"""
from threading import Thread
from queue import Queue
import time

queue = Queue()


class Producer(Thread):
    def run(self) -> None:
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = f"product{count}"
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)


class Consumer(Thread):
    def run(self) -> None:
        while True:
            if queue.qsize() > 100:
                for i in range(10):
                    msg = self.name + queue.get()
                    print(msg)
                time.sleep(1)


if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()
    producer.start()
    time.sleep(1)
    consumer.start()
