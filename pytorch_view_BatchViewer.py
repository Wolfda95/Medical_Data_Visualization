import torch
from batchviewer import view_batch

def pytorch(path):
    tensor = torch.load(path)
    print(tensor.shape)

    tensor = tensor[0,0,...]
    width = tensor.shape[0]
    hight = tensor.shape[1]

    view_batch(tensor, width=width, height=hight)

def pytorch_name(path, name):
    tensor = torch.load(path)
    hold = 0
    print(tensor)


    img = tensor[name]
    print(img.shape)
    print(type(img))


    #id = tensor["info"]
    #print(id)

    #classe = tensor["class"]
    #print(classe)

    img = img.permute(0, 2, 1)
    width = img.shape[1]
    hight = img.shape[2]

    view_batch(img, width=width, height=hight)


def pytorch_mask(path, name_img, name_mask, D):
    tensor = torch.load(path)

    img = tensor[name_img]
    mask = tensor[name_mask]
    print(img.shape)
    print(mask.shape)

    if D == True:
        img = img.permute(0, 2, 1)
        mask = mask.permute(0, 2, 1) #mask = mask.transpose(0, 2, 1)
        print(img.shape)
        print(mask.shape)
        width = img.shape[1]
        hight = img.shape[2]
        view_batch(img, mask, width=width, height=hight)

    if D == False:
        width = img.shape[0]
        hight = img.shape[1]
        view_batch(img, mask, width=width, height=hight)

def pytorch_mask_two(serie, mask):
    tensor_serie = torch.tensor(torch.load(serie))
    tensor_mask = torch.tensor(torch.load(mask))

    img = tensor_serie.permute(0, 2, 1)
    mask = tensor_mask.permute(0, 2, 1)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, mask, width=width, height=hight)