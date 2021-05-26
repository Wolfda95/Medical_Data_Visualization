import torch
from batchviewer import view_batch

def pytorch(path, name):
    tensor = torch.load(path)

    img = tensor[name]

    img = img.permute(0, 2, 1)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, width=width, height=hight)


def pytorch_mask(path, name_img, name_mask):
    tensor = torch.load(path)

    img = tensor[name_img]
    mask = tensor[name_mask]

    img = img.permute(0, 2, 1)
    mask = mask.permute(0, 2, 1)
    width = img.shape[1]
    hight = img.shape[2]
    view_batch(img, mask, width=width, height=hight)