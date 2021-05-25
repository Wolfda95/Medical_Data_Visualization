import dicom2nifti # pip install dicom2nifti

def dicom_to_nifti(input_path, output_path):

    dicom2nifti.convert_directory(input_path, output_path) # erzeugt .nii.gz Datei