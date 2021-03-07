import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.autograd import Variable
import sys, os

pretrain = '../../pretrain_model/20210217/vgg19/8_model.pth'
epoch = torch.load(pretrain)['epoch']
loss_lambda = torch.load(pretrain)['loss_lambda']
model_state_dict = torch.load(pretrain)['model_state_dict']
optimizer_state_dict = torch.load(pretrain)['optimizer_state_dict']
loss = torch.load(pretrain)['loss']
kill_loss = torch.load(pretrain)['kill_loss']
loss_lambda = torch.load(pretrain)['loss_lambda']
torch.save({'model_version': 'V5', 'epoch': epoch, 'model_state_dict': model_state_dict, 'optimizer_state_dict': optimizer_state_dict, 'loss': loss, 'kill_loss': kill_loss, 'loss_lambda': loss_lambda}, os.path.splitext(pretrain)[0] + '_modify' + os.path.splitext(pretrain)[1])







