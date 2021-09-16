# Batchviwer aus Git Herunterladen: https://github.com/FabianIsensee/BatchViewer und Anleitung in Readme durchführen
# Batchviewer Info: Im Bild scrollen: nur jede zweite Schicht | Neben Bild scrollen: jede Schicht

from dicom_view_BatchViewer import run_ct
from dicom_view_BatchViewer import run_ct_resize
from dicom_view_BatchViewer import run_ct_mask
from dicom_view_BatchViewer import run_mrt
from dicom_view_BatchViewer import run_mrt_resize
from dicom_view_BatchViewer import run_mrt_mask
from dicom_view_BatchViewer import run_mrt_dicom_mask

from nifti_view_BatchViewer import nifti_mrt
from nifti_view_BatchViewer import nifti_mrt_mask
from nifti_view_BatchViewer import nifti_ct
from nifti_view_BatchViewer import nifti_ct_mask
from nifti_view_BatchViewer import nifti_volume

from pytorch_view_BatchViewer import pytorch
from pytorch_view_BatchViewer import pytorch_name
from pytorch_view_BatchViewer import pytorch_mask
from pytorch_view_BatchViewer import pytorch_mask_two

from dicom_header import header

from dicom_nifti import dicom_to_nifti

from overlay import overlay_dicom_pytorch

def main():
    # Eine der blauen Zeilen einkommentieren (jenachdem was man ausgeben will)

    ########################################## BatchViewer DICOM ######################################################

    # ----------------------------- DICOM CT BatchViwer ------------------------------------------------
    # (CT_Pfad, Körperteil)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: run_ct("/home/wolfda/Clinic_Data/Data/Covid_Concern/Dicom/Python_Extract/0000100850/3990756/3", "lungs")

    # ----------------------------- DICOM CT BatchViwer + Resize to [48,256,256] --------------------------------------
    # (CT_Pfad, Körperteil)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
     # Todo: run_ct_resize('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs")

    # ----------------------------- DICOM CT BatchViwer + Nifti maske ------------------------------------------------
    # (CT_Pfad, Körperteil, NiftiMaske_Pfad)
    # Körperteil: abdomen, angio, bon, brain, chest, lungs
    # Todo: run_ct_mask('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3', "lungs", "/home/wolfda/Data_lifex/0000100850_0000100850_3990756_3/RoiVolume/R1.uint16.nii.gz")

    # ----------------------------- DICOM MRT BatchViwer ------------------------------------------------
    # Todo: run_mrt('/media/wolfda/XAIRAD-UKU/3')

    # ----------------------------- DICOM MRT BatchViwer + resize to [48,256,256] -------------------------------------
    # Todo: run_mrt_resize('/home/wolfda/Clinic_Data/Test/Prostata_Mamma/0008046191/3865644/6')

    # ----------------------------- DICOM MRT BatchViwer + Nifti Maske ------------------------------------------------
    # (CT_Pfad, NiftiMaske_Pfad)
    # Todo: run_mrt_mask('/home/wolfda/Clinic_Data/Data/Covid_Concern/Covid_CT_Kloth/0000100850/3990756/3',"/home/wolfda/Data_lifex/0000100850_0000100850_3990756_3/RoiVolume/R1.uint16.nii.gz")

    # ----------------------------- DICOM MRT BatchViwer + DICOM Maske ------------------------------------------------
    # (CT_Pfad, DICOMMaske_Pfad)
    # Todo: run_mrt_dicom_mask('/home/wolfda/Clinic_Data/Data/Leber/Python_readin/0000100441/3310375/0000100441gross',"/home/wolfda/Clinic_Data/Data/Leber/Python_readin/0000100441/3310375/1222")


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
    # Todo:  nifti_mrt("/home/wolfda/Data_lifex/0007890533_0007890533_3757035_5/RoiVolume/R1.uint16.nii.gz")

    # ----------------------------- Nifti MRT BatchViwer + Maske ------------------------------------------------
    # (MRT_Pfad, Maske_Pfad)
    # Todo: nifti_mrt_mask("/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_ct.nii.gz", "/home/wolfda/Clinic_Data/Challenge/Challenge_COVID-19-20_v2/Train/volume-covid19-A-0003_seg.nii.gz")

    # ----------------------------- Nifti 3d Volume------------------------------------------------
    #(Nifti Maske, Dicom Bild)
    nifti_volume("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/3D Volume/1mm/R1.uint16.nii.gz", "/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/3D Volume/1mm/3/000001_1.3.12.2.1107.5.1.4.96208.30000019111307071679700001478.dcm")

    ########################################## BatchViewer Pytorch Tensor #############################################
    # ----------------------------- Pytorch BatchViwer  ------------------------------------------------
    # (pytorch_path)
    # name: torch.save(image)
    # Todo:  pytorch("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/Data/Test_Data/0.pt")


    # ----------------------------- Pytorch BatchViwer (File in liste) ------------------------------------------------
    # (pytorch_path, name)
    # name: torch.save("vol": image, "id": ...) -> name = "vol"
    # Todo: pytorch_name("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/Data/Test_Data/0.pt", "vol")


    # ----------------------------- Pytorch BatchViwer + Maske (Bild und Maske in einer Liste) ------------------------------------------------
    # (pytorch_path, name_img, name_mask)
    # name: torch.save("vol": image, "mask": Maske)
    # Todo: pytorch_mask("/home/wolfda/Clinic_Data/Data/Leber/Python_net/48_800_800/train/0000100441.pt", "vol", "mask")

    # ----------------------------- Pytorch BatchViwer + Maske (Bild und Makse in 2 getrennten files)------------------------------------------------
    # (pytorch_image_path, pytorch_roi_path)
    # Todo: pytorch_mask_two("/home/wolfda/PycharmProjects/clinic-project-tracking/helper/serie.pt", "/home/wolfda/PycharmProjects/clinic-project-tracking/helper/mask.pt")


    ########################################## DICOM Header ###########################################################

    # ----------------------------- DICOM Header ------------------------------------------------
    # Todo: header("/home/wolfda/Clinic_Data/Data/Sarkome_Catharina/3D Volume/3757035/5/000001_1.3.12.2.1107.5.1.4.96208.30000019111307071679700002905.dcm")



    ########################################## DICOM / Nifti ##########################################################

    # ----------------------------- DICOM to Nifti ------------------------------------------------
    # Vorher herunterladen: pip install dicom2nifti
    # Vorher den Order erstellen in dem die Nifti Datei gespeichert werden soll (=save_folder)
    # (dicom_path, save_folder)
    # Todo: dicom_to_nifti("/home/wolfda/Clinic_Data/Test/Test_ROI_IMPAX/4078774/4078774", "/home/wolfda/Clinic_Data/Test/Test_ROI_IMPAX/4078774/4078774/nifti_test")
    # ACTUNG: Eventuell sind nach der umwandlung x,y,schichten im Tensor Vertauscht (z.B. statt (x,y, Anzahl Schichten) kommt danach (x,Anzahl Schichten,y) -> nach dem auslesen der Pixelwerte als Numpy array: img = img.transpose(1, 0, 2) )


    ########################################## Übereineander Legen ##########################################################

    # ----------------------------- DICOM Bild PyTorch Mask ------------------------------------------------
    # (Bild: dicom_path, Mask: pythorch path, Schicht)
    # Todo: overlay_dicom_pytorch("/home/wolfda/Clinic_Data/Data/Leber/Backup/0000100441/3310375/0000100441gross", "/home/wolfda/Clinic_Data/Data/Leber/Backup/0000100441/3310375/mask.pt", 45)



if __name__ == '__main__':
    main()
