# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午6:46
Author: ybx
"""

import multiprocessing
import time
import random
import os


def test1(msg):
    t_start = time.time()
    print("消息%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%消息s执行完成，耗时%.2f" % (msg, t_stop - t_start))


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for f in range(0, 10):
        pool.apply_async(test1, (f,))  # 每次循环的时候都会将空闲的 子进程去调用目标函数

    print('--------start-------')
    pool.close()  # 关闭进程池将是不会再接收请求了
    pool.join()  # 等待所有的pool中的子进程执行完成, 必须放在close(0 后面的

    print('------end-------')


