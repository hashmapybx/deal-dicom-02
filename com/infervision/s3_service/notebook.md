## test
    dcm_bucket.download_file(target_folder_value, os.path.join(dcm_out_path, dcm_name))
    target_folder_value = '96e72975-5dcc-4326-8956-33b8dbbf617e/CS757002-70003210-T100_206.dcm'
    dcm_out_path  = '/media/tx-eva-data/Data1/download_data_from_S3/data/2019-11-08_DATA-707/dicom/CS757002-70003210-T100'
    dcm_name = CS757002-70003210-T100_206.dcm
    
    
    关于requests 发送post请求的话 以form形式来提交数据的操作 只需要将请求的参数转化成一个字典 然后传给requests.post(url, data, headers) 
    
    
## 关于mysql 里面的字段datetime 类型的在插入数据的时候会报错 所以在插入数据的时候 datetime的类型字段必须要传入格式化的时间字符串就可以了
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 表示已经是字符串了 
    在执行insert 操作的时候直接传入字符串就ok了
    
    
        


    