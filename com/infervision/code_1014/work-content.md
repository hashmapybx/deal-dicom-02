## 会议内容记录
    临床预实验的数据量120例 中间脱落5例
    补相应的记录


## CE 
    总共是150例数据 detection:150  其中100例做lobe segmetion 标记
    原始数据库大于400多例
    基础400多例
    标记数据库: 150例 其中标记的时候也是要有脱落的
    
    
## PMDA 
    
    


## CFDA 
    lobe segmention 的数据检出记录 
    操作流程是先把在lobe和segmention里面的pid 但是不在detection里面的pid找到
    修改lobe里面的xml文件去除掉lobe的标签
    把这些数据按照医院的协议时间划分到detection的两批test数据
    
    

## 关于入库的自动化流程实现

    1. 目前的流程是给到的label 和dicom 首先需要计算dicomhash值并且写入到label标签内的数据 
    2. dicm的数需要统计source.csv的数据
    3. lael产生source文件 要注意层级目录  
    4. 启动jar进程来 通过Postman来发送postman来发送post请求
    
    
    
       
            
    