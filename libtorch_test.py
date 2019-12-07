import torch
from torch import nn


class MyNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Sequential(
            nn.Linear(784, 100),
            nn.ReLU(),
            nn.Linear(100, 10),
            nn.Softmax()
        )

    def forward(self, data):
        return self.layer(data)


if __name__ == '__main__':
    net = MyNet()
    # load weight
    # net.eval()

    traced_script_module = torch.jit.script(net)
    traced_script_module.save("traced_resnet_model.pt")
    print(torch.__version__)
