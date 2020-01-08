# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午5:54
Author: ybx
"""

from multiprocessing import Process, Queue
import time


def func1(queue):
    while True:
        info = queue.get()
        if info == None:
            return
        print(info)


def func2(queue):
    for i in range(10):
        time.sleep(1)
        queue.put('is %d' % i)
    queue.put(None)  # 结束的标志


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=func1, args=(q,))
    p2 = Process(target=func2, args=(q,))

    p1.start()
    p2.start()




