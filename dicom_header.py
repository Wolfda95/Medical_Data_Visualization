import pydicom as dicom  # DICOM Images (.dicom)

def header(path):

    dataset = dicom.read_file(path)

    print(dataset)



