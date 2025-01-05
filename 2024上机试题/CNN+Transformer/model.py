import torch.nn as nn
import torch


class AlexNet(nn.Module):
    def __init__(self, num_classes=1000, init_weights=False):
        super(AlexNet, self).__init__()
        # *** self.features的实现 ***
            # Conv1: input[3, 224, 224], output[48, 55, 55]
            # ReLU
            # Maxpool1: output[48, 27, 27]
            # Conv2: output[128, 27, 27]
            # ReLU
            # Maxpool2: output[128, 13, 13]
            # Conv3: output[192, 13, 13]
            # ReLU
            # Conv4: output[192, 13, 13]
            # ReLU
            # Conv5: output[128, 13, 13]
            # ReLU
            # Maxpool3: output[128, 6, 6]


        # *** self.classifier的实现 ***
            # dropout
            # FN1
            # RelU
            # dropout
            # FN2
            # RelU
            # FN3
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        # *** 模型前向过程的定义 ***
        # *** 通过self.features提取输入图像的特征 ***
        # *** 使用torch.flatten()将特征展平为适配分类器输入的形状 ***
        # *** 将特征输入self.classifier得到图像属于各个类别的概率 ***
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)
