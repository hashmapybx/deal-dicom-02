## 关于tensroflow里面的变量于神经网络里面的参数设置
    import tensorflow as tf 
    # 声明一个2*3 的矩阵变量
    weights = tf.variable(tf.random_normal[2,3], sttdev=2) # 标注差stddev 均值为0 
    这里的随机数函数有一下种类
        tf.random_normal 符合正太分布的随机数
        tf.truncated_normal 
        tf.random_uniform 均匀分布 
        tf.random_gamma 
    另外tensorflow 里面的变量也是可以通过常量constant 来进行初始化的操作的
    tf.zeros() 
    tf.ones() 
    bias 偏重项通常使用常熟来进行初始化的操作的
    tf.variable(tf.zeros(3)) 1*3的矩阵
    
    关于张量的概念  可以看成是向量把 它也具有维度和数据类型
    那么如何更好的tensorflow 里面设置参数呢?
    通过机器学习的监督学习;来设置参数的操作
    反向传播优化算法
    