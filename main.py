from dicom_view_BatchViewer import run_ct
from dicom_view_BatchViewer import run_mrt
from nifti_view_BatchViewer import nifti_mrt
from nifti_view_BatchViewer import nifti_ct
from dicom_header import header

def main():

    ########################################## BatchViewer ###########################################################

    # ----------------------------- DICOM CT BatchViwer ------------------------------------------------
    # abdomen, angio, bon, brain, chest, lungs
    #run_ct('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs")

    # ----------------------------- DICOM MRT BatchViwer ------------------------------------------------
    #run_mrt('/home/wolfda/Clinic_Data/Test/Prostata_Mamma/0008046191/3865644/6')

    # ----------------------------- Nifti CT BatchViwer ------------------------------------------------
    # abdomen, angio, bon, brain, chest, lungs
    #nifti_ct("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz", "lungs")

    # ----------------------------- Nifti MRT BatchViwer ------------------------------------------------
    #nifti_ct("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz")


    ########################################## Header ################################################################

    # ----------------------------- DICOM Header ------------------------------------------------
    header("/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3/000001_1.3.12.2.1107.5.1.4.122102.30000020100907291877200016274.dcm")



if __name__ == '__main__':
    main()
