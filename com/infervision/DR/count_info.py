# -*- coding: utf-8 -*-
"""
Create Time: 2019/10/9 下午4:14
Author: ybx
"""
import os
import sys
import pydicom
import pandas as pd

path = "/media/tx-eva-data/Data1/pachong/dcm"
save_path = '/media/tx-eva-data/Data1/pachong/dcm'
id_list = []
KVP_list = []
XRayTubeCurrent_list = []
bodypart_list = []
convolutionKernel_list = []
slice_list = []
dose_list = []
age_list = []
Manufacturer_list = []
ManufacturerModelName_list = []
sex_list = []
Exposure_list = []
wc_list = []
ww_list = []
LargestImage = []
studydate_list = []
studytime_list = []
SmallestImage_list = []
hospital_name_list = []
PixelSpacing_list = []
PatientDate_list = []
accession_list = []
WCWW_list = []
studyuid_list = []
seruid_list = []
Smallest_list = []
Largest_list = []
count = 0
folder_List = []
sop_list = []

for h_folder in os.listdir(path):

    h_folder_path = os.path.join(path, h_folder)
    for b_folder in os.listdir(h_folder_path):

        b_folder_path = os.path.join(h_folder_path, b_folder)  # 批次
        for p_folder in os.listdir(b_folder_path):
            folder_path = os.path.join(b_folder_path, p_folder)  # pid
            for study_folder in os.listdir(folder_path):
                study_folder_path = os.path.join(folder_path, study_folder)  # study_uid
                try:
                    # for series_id in os.listdir(study_folder_path):
                    #     series_id_path = os.path.join(study_folder_path, series_id) #seried_uid /dicom
                    try:
                        for dcm_file in os.listdir(study_folder_path):
                            count += 1
                            dcm_file_path = os.path.join(study_folder_path, dcm_file)
                            ds = pydicom.read_file(dcm_file_path, force=True, stop_before_pixels=True)
                            try:
                                PatientAge = ds.PatientAge
                            except:
                                PatientAge = "N/A"
                            try:
                                kvp = ds.KVP
                            except:
                                kvp = "N/A"
                            try:
                                XRayTubeCurrent = ds.XRayTubeCurrent
                            except:
                                XRayTubeCurrent = "N/A"
                            try:
                                convolutionKernel = ds.ConvolutionKernel
                            except:
                                convolutionKernel = "N/A"
                            try:
                                sliceThickness = ds.SliceThickness
                            except:
                                sliceThickness = "N/A"
                            try:
                                PixelSpacing = ds.PixelSpacing
                            except:
                                PixelSpacing = "N/A"
                            try:
                                Manufacturer = ds.Manufacturer
                            except:
                                Manufacturer = "N/A"
                            try:
                                ManufacturerModelName = ds.ManufacturerModelName
                            except:
                                ManufacturerModelName = "N/A"
                            try:
                                PatientSex = ds.PatientSex
                            except:
                                PatientSex = "N/A"
                            try:
                                ID = ds.PatientID
                            except:
                                ID = "N/A"
                            try:
                                AccessionNumber = ds.AccessionNumber
                            except:
                                AccessionNumber = "N/A"
                            try:
                                StudyDate = ds.StudyDate
                            except:
                                StudyDate = "N/A"
                            try:
                                StudyTime = ds.StudyTime
                            except:
                                StudyTime = "N/A"
                            try:
                                WindowCenter = str(ds.WindowCenter)
                            except:
                                WindowCenter = "N/A"
                            try:
                                WindowWidth = str(ds.WindowWidth)
                            except:
                                WindowWidth = "N/A"
                            # print(dcm_file_path)
                            StudyInstanceUID = ds.StudyInstanceUID
                            SeriesInstanceUID = ds.SeriesInstanceUID
                            SOPInstanceUID = ds.SOPInstanceUID
                            try:
                                PatientDate = ds.PatientBirthDate
                            except:
                                PatientDate = "N/A"
                            try:
                                BodyPartExamined = ds.BodyPartExamined
                            except:
                                BodyPartExamined = "N/A"

                            try:
                                LargestImagePixelValue = ds.LargestImagePixelValue
                            except:
                                LargestImagePixelValue = "N/A"
                            try:
                                SmallestImagePixelValue = ds.SmallestImagePixelValue
                            except:
                                SmallestImagePixelValue = "N/A"
                            try:
                                WW = ds.WindowCenterWidthExplanation
                            except:
                                WW = "N/A"
                            id_list.append(str(ID))
                            folder_List.append(p_folder)
                            sop_list.append(SOPInstanceUID)
                            accession_list.append(AccessionNumber)
                            sex_list.append(PatientSex)
                            age_list.append(PatientAge)
                            PatientDate_list.append(PatientDate)
                            studydate_list.append(StudyDate)
                            studytime_list.append(StudyTime)
                            studyuid_list.append(StudyInstanceUID)
                            seruid_list.append(SeriesInstanceUID)
                            Manufacturer_list.append(Manufacturer)
                            ManufacturerModelName_list.append(ManufacturerModelName)
                            bodypart_list.append(BodyPartExamined)
                            slice_list.append(sliceThickness)
                            KVP_list.append(kvp)
                            XRayTubeCurrent_list.append(XRayTubeCurrent)
                            convolutionKernel_list.append(convolutionKernel)
                            PixelSpacing_list.append(PixelSpacing)
                            Smallest_list.append(SmallestImagePixelValue)
                            Largest_list.append(LargestImagePixelValue)
                            wc_list.append(WindowCenter)
                            ww_list.append(WindowWidth)
                            WCWW_list.append(WW)
                            break
                    except:
                        count += 1
                        # dcm_file_path = os.path.join(series_id_path, dcm_file)
                        try:
                            ds = pydicom.read_file(dcm_file_path)
                        except:
                            print(dcm_file_path)
                            break
                        try:
                            PatientAge = ds.PatientAge
                        except:
                            PatientAge = "N/A"
                        try:
                            kvp = ds.KVP
                        except:
                            kvp = "N/A"
                        try:
                            XRayTubeCurrent = ds.XRayTubeCurrent
                        except:
                            XRayTubeCurrent = "N/A"
                        try:
                            convolutionKernel = ds.ConvolutionKernel
                        except:
                            convolutionKernel = "N/A"
                        try:
                            sliceThickness = ds.SliceThickness
                        except:
                            sliceThickness = "N/A"
                        try:
                            PixelSpacing = ds.PixelSpacing
                        except:
                            PixelSpacing = "N/A"
                        try:
                            Manufacturer = ds.Manufacturer
                        except:
                            Manufacturer = "N/A"
                        try:
                            ManufacturerModelName = ds.ManufacturerModelName
                        except:
                            ManufacturerModelName = "N/A"
                        try:
                            PatientSex = ds.PatientSex
                        except:
                            PatientSex = "N/A"
                        try:
                            ID = ds.PatientID
                        except:
                            ID = "N/A"
                        try:
                            AccessionNumber = ds.AccessionNumber
                        except:
                            AccessionNumber = "N/A"
                        try:
                            StudyDate = ds.StudyDate
                        except:
                            StudyDate = "N/A"
                        try:
                            StudyTime = ds.StudyTime
                        except:
                            StudyTime = "N/A"
                        try:
                            WindowCenter = str(ds.WindowCenter)
                        except:
                            WindowCenter = "N/A"
                        try:
                            WindowWidth = str(ds.WindowWidth)
                        except:
                            WindowWidth = "N/A"
                        # print(dcm_file_path)
                        StudyInstanceUID = ds.StudyInstanceUID
                        SeriesInstanceUID = ds.SeriesInstanceUID
                        SOPInstanceUID = ds.SOPInstanceUID
                        try:
                            PatientDate = ds.PatientBirthDate
                        except:
                            PatientDate = "N/A"
                        try:
                            BodyPartExamined = ds.BodyPartExamined
                        except:
                            BodyPartExamined = "N/A"

                        try:
                            LargestImagePixelValue = ds.LargestImagePixelValue
                        except:
                            LargestImagePixelValue = "N/A"
                        try:
                            SmallestImagePixelValue = ds.SmallestImagePixelValue
                        except:
                            SmallestImagePixelValue = "N/A"
                        try:
                            WW = ds.WindowCenterWidthExplanation
                        except:
                            WW = "N/A"
                        id_list.append(str(ID))
                        folder_List.append(p_folder)
                        sop_list.append(SOPInstanceUID)
                        accession_list.append(AccessionNumber)
                        sex_list.append(PatientSex)
                        age_list.append(PatientAge)
                        PatientDate_list.append(PatientDate)
                        studydate_list.append(StudyDate)
                        studytime_list.append(StudyTime)
                        studyuid_list.append(StudyInstanceUID)
                        seruid_list.append(SeriesInstanceUID)
                        Manufacturer_list.append(Manufacturer)
                        ManufacturerModelName_list.append(ManufacturerModelName)
                        bodypart_list.append(BodyPartExamined)
                        slice_list.append(sliceThickness)
                        KVP_list.append(kvp)
                        XRayTubeCurrent_list.append(XRayTubeCurrent)
                        convolutionKernel_list.append(convolutionKernel)
                        PixelSpacing_list.append(PixelSpacing)
                        Smallest_list.append(SmallestImagePixelValue)
                        Largest_list.append(LargestImagePixelValue)
                        wc_list.append(WindowCenter)
                        ww_list.append(WindowWidth)
                        WCWW_list.append(WW)
                        break
                except:
                    count += 1
                    # dcm_file_path = os.path.join(series_id_path, dcm_file)
                    try:
                        ds = pydicom.read_file(study_folder_path)
                    except:
                        print(study_folder_path)
                        break
                    try:
                        PatientAge = ds.PatientAge
                    except:
                        PatientAge = "N/A"
                    try:
                        kvp = ds.KVP
                    except:
                        kvp = "N/A"
                    try:
                        XRayTubeCurrent = ds.XRayTubeCurrent
                    except:
                        XRayTubeCurrent = "N/A"
                    try:
                        convolutionKernel = ds.ConvolutionKernel
                    except:
                        convolutionKernel = "N/A"
                    try:
                        sliceThickness = ds.SliceThickness
                    except:
                        sliceThickness = "N/A"
                    try:
                        PixelSpacing = ds.PixelSpacing
                    except:
                        PixelSpacing = "N/A"
                    try:
                        Manufacturer = ds.Manufacturer
                    except:
                        Manufacturer = "N/A"
                    try:
                        ManufacturerModelName = ds.ManufacturerModelName
                    except:
                        ManufacturerModelName = "N/A"
                    try:
                        PatientSex = ds.PatientSex
                    except:
                        PatientSex = "N/A"
                    try:
                        ID = ds.PatientID
                    except:
                        ID = "N/A"
                    try:
                        AccessionNumber = ds.AccessionNumber
                    except:
                        AccessionNumber = "N/A"
                    try:
                        StudyDate = ds.StudyDate
                    except:
                        StudyDate = "N/A"
                    try:
                        StudyTime = ds.StudyTime
                    except:
                        StudyTime = "N/A"
                    try:
                        WindowCenter = str(ds.WindowCenter)
                    except:
                        WindowCenter = "N/A"
                    try:
                        WindowWidth = str(ds.WindowWidth)
                    except:
                        WindowWidth = "N/A"
                    # print(dcm_file_path)
                    StudyInstanceUID = ds.StudyInstanceUID
                    SeriesInstanceUID = ds.SeriesInstanceUID
                    SOPInstanceUID = ds.SOPInstanceUID
                    try:
                        PatientDate = ds.PatientBirthDate
                    except:
                        PatientDate = "N/A"
                    try:
                        BodyPartExamined = ds.BodyPartExamined
                    except:
                        BodyPartExamined = "N/A"

                    try:
                        LargestImagePixelValue = ds.LargestImagePixelValue
                    except:
                        LargestImagePixelValue = "N/A"
                    try:
                        SmallestImagePixelValue = ds.SmallestImagePixelValue
                    except:
                        SmallestImagePixelValue = "N/A"
                    try:
                        WW = ds.WindowCenterWidthExplanation
                    except:
                        WW = "N/A"
                    id_list.append(str(ID))
                    folder_List.append(p_folder)
                    sop_list.append(SOPInstanceUID)
                    accession_list.append(AccessionNumber)
                    sex_list.append(PatientSex)
                    age_list.append(PatientAge)
                    PatientDate_list.append(PatientDate)
                    studydate_list.append(StudyDate)
                    studytime_list.append(StudyTime)
                    studyuid_list.append(StudyInstanceUID)
                    seruid_list.append(SeriesInstanceUID)
                    Manufacturer_list.append(Manufacturer)
                    ManufacturerModelName_list.append(ManufacturerModelName)
                    bodypart_list.append(BodyPartExamined)
                    slice_list.append(sliceThickness)
                    KVP_list.append(kvp)
                    XRayTubeCurrent_list.append(XRayTubeCurrent)
                    convolutionKernel_list.append(convolutionKernel)
                    PixelSpacing_list.append(PixelSpacing)
                    Smallest_list.append(SmallestImagePixelValue)
                    Largest_list.append(LargestImagePixelValue)
                    wc_list.append(WindowCenter)
                    ww_list.append(WindowWidth)
                    WCWW_list.append(WW)
                    break


writer = pd.ExcelWriter(save_path + '/' + 'info.xls', encoding='unicode_escape')
df = pd.DataFrame(data={'ID': id_list, 'Age': age_list, 'AccessionNumber': accession_list,
                        'ConvolutionKernel': convolutionKernel_list, 'originalFolderName': folder_List,
                        'KVP': KVP_list, 'XRayTubeCurrent': XRayTubeCurrent_list, 'SOPInstanceUID': sop_list,
                        'Manufacturer': Manufacturer_list, 'ManufacturerModelName': ManufacturerModelName_list,
                        'PatientSex': sex_list, 'PixelSpacing': PixelSpacing_list,
                        'PatientBirthDate': PatientDate_list, 'WindowCenter': wc_list, 'WindowWidth': ww_list,
                        'WindowCenter&WidthExplanation': WCWW_list, "StudyDate": studydate_list,
                        'StudyTime': studytime_list,
                        'LargestImagePixelValue': Largest_list, 'SmallestImagePixelValue': Smallest_list,
                        'BodyPartExamined': bodypart_list, "SliceThickness": slice_list})





df.to_excel(writer, index=False)
writer.save()
print(count)
