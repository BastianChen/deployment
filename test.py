import torch
from torch import nn


class MyNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.seq = nn.Sequential(
            nn.Linear(784, 100),
            nn.ReLU(),
            nn.Linear(100, 10),
            nn.Softmax()
        )

    def forward(self, x):
        return self.seq(x)


if __name__ == '__main__':
    mynet = MyNet()
    #load weight
    mynet.eval()

    traced_script_module = torch.jit.script(mynet)
    traced_script_module.save("traced_mynet_model.pt")
