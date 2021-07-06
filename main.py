# Batchviwer aus Git Herunterladen: https://github.com/FabianIsensee/BatchViewer und Anleitung in Readme durchführen
# Batchviewer Info: Im Bild scrollen: nur jede zweite Schicht | Neben Bild scrollen: jede Schicht

from dicom_view_BatchViewer import run_ct
from dicom_view_BatchViewer import run_ct_resize
from dicom_view_BatchViewer import run_ct_mask
from dicom_view_BatchViewer import run_mrt
from dicom_view_BatchViewer import run_mrt_resize
from dicom_view_BatchViewer import run_mrt_mask

from nifti_view_BatchViewer import nifti_mrt
from nifti_view_BatchViewer import nifti_mrt_mask
from nifti_view_BatchViewer import nifti_ct
from nifti_view_BatchViewer import nifti_ct_mask

from pytorch_view_BatchViewer import pytorch
from pytorch_view_BatchViewer import pytorch_mask

from dicom_header import header

from dicom_nifti import dicom_to_nifti

def main():
    # Eine der blauen Zeilen einkommentieren (jenachdem was man ausgeben will)

    ########################################## BatchViewer DICOM ######################################################

    # ----------------------------- DICOM CT BatchViwer ------------------------------------------------
    # (CT_Pfad, Körperteil)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: run_ct('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs")

    # ----------------------------- DICOM CT BatchViwer + Resize to [48,256,256] --------------------------------------
    # (CT_Pfad, Körperteil)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
     # Todo: run_ct_resize('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs")

    # ----------------------------- DICOM CT BatchViwer + Nifti maske ------------------------------------------------
    # (CT_Pfad, Körperteil, NiftiMaske_Pfad)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: run_ct_mask('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs", "/home/wolfda/Data_lifex/0000100850_0000100850_3990756_3/RoiVolume/R1.uint16.nii.gz")

    # ----------------------------- DICOM MRT BatchViwer ------------------------------------------------
    # Todo: run_mrt('/home/wolfda/Clinic_Data/Test/Prostata_Mamma/0008046191/3865644/6')

    # ----------------------------- DICOM MRT BatchViwer + resize to [48,256,256] -------------------------------------
    # Todo: run_mrt_resize('/home/wolfda/Clinic_Data/Test/Prostata_Mamma/0008046191/3865644/6')

    # ----------------------------- DICOM MRT BatchViwer + Nifti Maske ------------------------------------------------
    # (CT_Pfad, NiftiMaske_Pfad)
    # Todo: run_mrt_mask('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3',"/home/wolfda/Data_lifex/0000100850_0000100850_3990756_3/RoiVolume/R1.uint16.nii.gz")



    ########################################## BatchViewer Nifti ######################################################

    # ----------------------------- Nifti CT BatchViwer------------------------------------------------
    # (CT_Pfad, Körperteil)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: nifti_ct("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz", "lungs")

    # ----------------------------- Nifti CT BatchViwer + Maske------------------------------------------------
    # (CT_Pfad, Körperteil, Maske_Pfad)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: nifti_ct_mask("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz", "lungs", "/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_seg.nii.gz")

    # ----------------------------- Nifti MRT BatchViwer ------------------------------------------------
    # Todo: nifti_mrt("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz")

    # ----------------------------- Nifti MRT BatchViwer + Maske ------------------------------------------------
    # (MRT_Pfad, Maske_Pfad)
    # Todo: nifti_mrt_mask("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz", "/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_seg.nii.gz")



    ########################################## BatchViewer Pytorch Tensor #############################################

    # ----------------------------- Pytorch BatchViwer ------------------------------------------------
    # (pytorch_path, name)
    # name: torch.save("vol": image, "id": ...) -> name = "vol"
    # Todo: pytorch("/home/wolfda/Clinic_Data/Data/Covid_Concern/Klassen/Beatmung/0000106246_2.pt", "vol")


    # ----------------------------- Pytorch BatchViwer + Maske ------------------------------------------------
    # (pytorch_path, name_img, name_mask)
    # name: torch.save("vol": image, "mask": Maske)
    # Todo: pytorch_mask("/home/wolfda/Clinic_Data/Data/Covid_Concern/Klassen/Beatmung/0000106246_2.pt", "vol", "mask")



    ########################################## DICOM Header ###########################################################

    # ----------------------------- DICOM Header ------------------------------------------------
    # Todo: header("/media/wolfda/diskAshur2/Lohrenz/0003134365/1286468/999999/999999_2.25.266590992388813470226041125580162655146.dcm")



    ########################################## DICOM / Nifti ##########################################################

    # ----------------------------- DICOM to Nifti ------------------------------------------------
    # Vorher herunterladen: pip install dicom2nifti
    # Vorher den Order erstellen in dem die Nifti Datei gespeichert werden soll (=save_folder)
    # (dicom_path, save_folder)
    # Todo: dicom_to_nifti("/home/wolfda/Clinic_Data/Test/Test_ROI_IMPAX/4078774/4078774", "/home/wolfda/Clinic_Data/Test/Test_ROI_IMPAX/4078774/4078774/nifti_test")
    # ACTUNG: Eventuell sind nach der umwandlung x,y,schichten im Tensor Vertauscht (z.B. statt (x,y, Anzahl Schichten) kommt danach (x,Anzahl Schichten,y) -> nach dem auslesen der Pixelwerte als Numpy array: img = img.transpose(1, 0, 2) )



if __name__ == '__main__':
    main()
