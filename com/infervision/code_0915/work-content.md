## 2019年 09月 15日 星期日 15:36:19 CST
    
    和楚哥讨论关于脱落记录表的生成
    关于 脱落表的生成逻辑是按标注记录表的月为时间单位去生成
    把裱标注记录表里面的时间按照月读取到list里面  这个list中可能包含好几个医院的数据
    每个脱落表的数据量在120 的上下范围波动  看每个月的数据量的情况
    另外还需要六分之一的脱落数据的id  这些数据就是要到对应的医院的tmp文件下面去读取 数据量的分配是120的六分之一的上下10 的范围波动
    
    开始写代码
    
    

## 2019年 09月 16日 星期一 10:14:39 CST
   
    早晨完成数据脱落筛选记录表
     
     

## 2019年 09月 20日 星期五 10:27:18 CST
    在tensorflow 里面的变量 运算 张量tensor collection集合 
    collection中   当我们在一个运算中定义的变量最终是都会到集合里面去的
    import tensorflow as tf
    tf.Variable() 这个表示的是一个运算操作
    当我们在程序中定义变量都是需要初始化之后才可以使用的 
    变量的初始化在tensorflow 里面是可以通过随机函数random_normal 产生符合正态分布的随机数来填充矩阵 
    或者是常数生成函数
    tf.zeros 
    tf.ones([2,3]) 产生一个全是1的数组 2*3 矩阵 
    tf.fill([2,3], 9) 产生一个2*3的矩阵全部用9来填充
    tf.constant([1,2,3]) 产生一个数组


    淄博市人民医院数据入库
    克拉玛数据入库 
    CFDA相关文件的整理完善
    

