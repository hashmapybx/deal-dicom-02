##  修改mysql的密码 
    mysql的版本信息:5.7.27
    首先需要修改 /etc/mysql/my.cnf 文件
    在文本末尾加上
    [mysqld]
    skip-grant-tables
    1)、use mysql;                   #连接到mysql数据库
    2)、update mysql.user set authentication_string=password('123456') where user='root' and Host ='localhost';    #修改密码123456是密码
    3)、update user set  plugin="mysql_native_password";     
    4)、flush privileges;
    5)、quit; 
    
    
## 修改CFDA数据库的文件 上传时间
    


## 问题记录 
    上传到58 的数据 大连中山的 数据上传位置有问题  脑缺血的 要发放到strock 下面去
    
    
## python
    os.walk方法，主要用来遍历一个目录内各个子目录和子文件。 
    该方法返回的是一个三元组(dirpath, dirnames, filenames) 
    其中 dirpath: 表示的是起始路径
    dirnames 是一个list集合 表示起始路径下面的所有子文件夹
    filenames 是 起始路径下所有的文件名             
        
        
##   2019年 09月 26日 星期四 14:03:01 CST
    早晨处理数据克拉玛依骨折数据的注释量 把数据库之前上传的删除掉重新上传数据  总的数据量是51套
    下午处理鼓楼的假阳反馈数据
    
    
   关于数据入库的操作的一些想法
   目前存在的问题
## Tue Oct 29 10:10:56 CST 2019 
    完成了mysite的入库操作流程的开发
    
    关于shalong的数据的定时清理脚本
    关于脚本的流程
    首先要去检查本地的shalong文件夹中和server上面的文件夹中的数据去做对比 截止最大日期的两天前 在删除更早的数据
    
    linux下面的shell script 执行的两种方式 一种是新产生一个shell 另一中是在当前的shell下面来执行 不在启动一个shell
      那么新产生一个shell来执行的操作是在啊script的开头加入 #!/bin/sh 这种方式是会新启动一个子进程来执行 
      source:  其实就是.命令 代表当前路径
      exec: man exec 可以看到linux解释说这个命令是no process is cretaed 也就是说不会产生新的子进程 那么于上面的source有什么区别呢?
      exec命令在执行时会把当前的shell process关闭掉, 然后在切换到执行后面的命令 例如: exec ls -l {} \;
      
      system和exec的区别
      exec实际上是直接用新的进程来代替前面执行的进程环境 在来执行后面的命令 运行之后是不会返回原来的进程中去的
      system是shell调用你的命令 执行完毕是会回到原来的进程中的
      
      
    
    
    
    
    
    
    
    
    
       

   
    
    
    
    
    
           