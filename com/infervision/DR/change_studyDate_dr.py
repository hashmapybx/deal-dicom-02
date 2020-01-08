import os
import pydicom

path = "/media/tx-eva-data/CE_DR/基础数据库/train_data_2634/中国人民解放军陆军军医大学第一附属医院/error"
for folders_path, folders, files in os.walk(path):
    for file in files:
        dcm_path = os.path.join(folders_path, file)
        info = pydicom.read_file(dcm_path)
        info = pydicom.read_file(dcm_path, force=True)
        info.Manufacturer = 'SIEMENS'
        # try:
        #     info.StudyDate = str(int(str(info.StudyDate).strip()) - 10000)
        #     info.SeriesDate = str(int(str(info.SeriesDate).strip()) - 10000)
        #     # info.AcquisitionDate = str(int(str(info.AcquisitionDate).strip()) - 10000)
        #     info.ContentDate = str(int(str(info.ContentDate).strip()) - 10000)
        # except:
        #     pass

        # info.PerformedProcedureStepStartDate = str(int(str(info.PerformedProcedureStepStartDate).strip()) - 10000)
        info.save_as(dcm_path)




