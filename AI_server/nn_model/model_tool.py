import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.autograd import Variable
import sys


class model_parameter_operation():

    def __init__(self):  # Run it once
        pass

    def gaussian_weights_init(self, m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1 and classname.find('Conv') == 0:
            m.weight.data.normal_(0.0, 0.02)

    def linear_input(self, shape):
        bs = 1
        input = Variable(t.rand(bs, *shape))
        output_feat = self._forward_features(input)
        n_size = output_feat.data.view(bs, -1).size(1)
        return n_size

    def _forward_features(self, x):
        out = self.cnn_encoder(x)
        return out


# model_tool.model_parameter_operation()


