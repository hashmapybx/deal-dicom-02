# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/15 下午6:02
Author: ybx
"""

from multiprocessing import Pool
import time, random, os


def func(n):
    pid = os.getpid()
    print('进程%s正在处理第%d个任务' % (pid, n), '时间%s' % time.strftime('%H-%M-%S'))
    time.sleep(2)
    res = '处理%s' % random.choice(['成功', '失败'])
    return res


def foo(info):
    print(info)  # 传入值为进程执行结果


if __name__ == '__main__':
    p = Pool(4)
    li = []
    for i in range(10):
        res = p.apply_async(func, args=(i,), callback=foo)  # callback()回调函数会在进程执行完之后调用（主进程调用）
        li.append(res)

    p.close()
    p.join()
    for i in li:
        print(i.get())
