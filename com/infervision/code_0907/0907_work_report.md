## 0907 需要完成的内容
    1.修改清洗记录表里面的对应医院的数据量
    2.修改脱敏记录里面的数据量
    3.修改回传记录表中的数据量
    4.重新修改原始和基础数据库中的文件系统数据touch -d "time" file
    
    关于标注记录里面的记录到PID
    detection 里面每一个医生每天标注量 并且对应到具体的PID的 其中审核人要换成审核医生
    要生成每一个医生一个excel表的话
    首先是要根据一条标注医生的记录找到在标注数据库中找到对应的医院的数据 
      标注医生  ：只能标注
      审核医生 ：既可以标注也可以审核
      仲裁医生： 仲裁是只做仲裁的事情 当每一天的标注结果中需要仲裁的数据量非常少的时候 可以累计一两天的结果来一起仲裁
      
## 0908 德化数据解压
    德化县医院 七月份的 DR清洗上传 解压完总共是:1904套
    
    数据脱敏依据 
    主要是替换掉病人和医生的相关信息
    
    
## 在做detection的时候 test 里面的anno 需要从    /media/tx-eva-data/NAS/new_addData/备份_不要删  这个路径下面来补充的做的 

      

      
       
    