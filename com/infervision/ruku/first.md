## 关于数据入库的说明
   
   对于dicom数据的csv生成文件和label的csv生成文件
   数据入库对应的rabbitmq的界面是192.168.130.81:15672
## 关于ubuntu下面的zip压缩文件解码乱码的问题
    unzip -O CP936 xx.zip

## 关于pandas里面的read_csv函数的说明
    read_csv函数里面的参数是
    pandas.read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None）
    
    sep=','   # 以，为数据分隔符
    shkiprows= 10   # 跳过前十行
    nrows = 10   # 只去前10行
    parse_dates = ['col_name']   # 指定某行读取为日期格式
    index_col = ['col_1','col_2']   # 读取指定的几列
    error_bad_lines = False   # 当某行数据有问题时，不报错，直接跳过，处理脏数据时使用
    na_values = 'NULL'   # 将NULL识别为空值
    header 默认是0 行作为列索引
    
   
## git 的相关操作 
    下面的命令是在报错的时候会出现的:
    To ssh://code.infervision.com:2022/data-group/ruku.git
     ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'ssh://git@code.infervision.com:2022/data-group/ruku.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    是因为远程的README.md文件没有关联到本地
    
    这个命令是把远程的repositiory 拉取到本地 进行覆盖 在把本地的提交
    git pull --rebase origin master
    另外一般在解决git上传时候的冲突的时候
    推荐是
    git push origin master -f 强制把本地的代码提交到远程的repository里面去
    
    
    标注数据库的数据量:
    detection
        test:  188+198 = 386
        train: 7043 + 3088 + 2856 + 1555=14542
    lobe:
         test: 145 
         train: 428+211=639 
    segmention:
          test:   267
          train:  2998     
    
    
   
   
   
   