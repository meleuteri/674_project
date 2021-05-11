import MinkowskiEngine as ME
import MakeData
import torch.nn as nn
from torch.utils.data import DataLoader
import torch

class MyNetwork(ME.MinkowskiNetwork):
    def __init__(self, in_feat, out_feat, D):
        super(MyNetwork, self).__init__(D)
        self.conv1 = nn.Sequential(
            ME.MinkowskiConvolution(
                in_channels=in_feat,
                out_channels=64,
                kernel_size=3,
                stride=2,
                dilation=1,
                bias=False,
                dimension=D),
            ME.MinkowskiBatchNorm(64),
            ME.MinkowskiReLU())
        self.conv2 = nn.Sequential(
            ME.MinkowskiConvolution(
                in_channels=64,
                out_channels=128,
                kernel_size=3,
                stride=2,
                dimension=D),
            ME.MinkowskiBatchNorm(128),
            ME.MinkowskiReLU())
        self.pooling = ME.MinkowskiGlobalPooling()
        self.linear = ME.MinkowskiLinear(128, out_feat)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.pooling(out)
        return self.linear(out)

train_dataset = MakeData.MakeData('dales_txt/train/')
train_dataloader = DataLoader(dataset=train_dataset, collate_fn=ME.utils.batch_sparse_collate)

net = MyNetwork(in_feat=3, out_feat=1000, D=3)

def my_loss(output, target):
    loss_arr = torch.zeros(output.shape)
    for i in range(output.shape[0]):
        if output[i] != target[i]:
            loss_arr[i] =1
        else:
            loss_arr[i] = 0
    return loss_arr

for coords, feats, label in iter(train_dataloader):
    v_input = ME.SparseTensor(coordinates=coords, features=feats, requires_grad=True) 
    output = net(v_input)
    loss = my_loss(output.F.squeeze(), label.long())  
    print("loss:")
    print(torch.sum(loss))
    loss.backward()

torch.save(net.state_dict(), 'net_state_dict.pt')
