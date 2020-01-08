# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午7:00
Author: ybx
"""
import os
import multiprocessing
import time


def write(q):
    print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "python":
        q.put(i)


def read(q):
    print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("read从Queue获取到消息：%s" % q.get(True))



if __name__ == "__main__":
    print("(%s) start" % os.getpid())
    q = multiprocessing.Manager().Queue() # 这个是用于进程池中的队列通信的
    q1 = multiprocessing.Queue()
    po = multiprocessing.Pool()
    po.apply_async(write, args=(q,))

    time.sleep(2)

    po.apply_async(read, args=(q,))
    po.close()
    po.join()

    print("(%s) end" % os.getpid())




