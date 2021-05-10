import os
import torch
import MakeData
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import MinkowskiEngine as ME

device = 'cpu'
print('Using {} device'.format(device))

if __name__ == "__main__":
    X_train = MakeData.MakeData('dales_txt/train/')
    print(len(X_train))# should be 29

    # train_dataloader = DataLoader(X_train, collate_fn=ME.utils.SparseCollation())
    # train_features, train_labels = next(iter(train_dataloader))
    # print(train_features[0])
    # print(train_labels[0])




