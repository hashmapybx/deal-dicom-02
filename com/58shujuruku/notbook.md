
## 关于数据下载的sql语句操作：
SELECT * FROM `t_dicom_information`


SELECT count(remote_path) FROM t_dicom_information where DATE_FORMAT(create_date, '%Y-%m-%d')='2019-08-30';

select * from t_batch_information where batch_name = '2019-08-30_DATA-149';


SELECT *  from t_dicom_collect_mark_purpose where DATE_FORMAT(create_date, '%Y-%m-%d')='2019-08-30';

SELECT * from t_dicom_collect where dicom_hospital_batch_id=150013;


select * from t_label_set where label_batch_id=150013;

select B.label_path, C.remote_path from t_label_information as B join 
(select label_set_id, dicom_set_id from t_label_set where label_batch_id =
(select batch_id from t_batch_information where batch_name= '2019-08-30_DATA-149')) as A  on A.label_set_id = B.label_set_Id join t_dicom_information as C  on A.dicom_set_id = C.collect_id;