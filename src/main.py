# Author: Utku Ozbulak
# utku.ozbulak@gmail.com

import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision import transforms
from model_cnn import MnistCNNModel
from data_loader import load_data
from data_loader import CustomImageDataset

z = 1

transformations = transforms.Compose([transforms.ToTensor()])

custom_mnist_dataset = CustomImageDataset('/home/ut/git/pytorch-experiments/data/mnist/train.csv',
                                    '/home/ut/git/pytorch-experiments/data/mnist/train',
                                    transformations)

custom_imagenet_dataset = CustomImageDataset('/home/ut/git/pytorch-experiments/data/imagenet_classes.csv',
                                    '/home/ut/git/pytorch-experiments/data/imagenet_images',
                                    transformations)

custom_dataset_loader = torch.utils.data.DataLoader(dataset=custom_imagenet_dataset, batch_size=10, shuffle=False)

model = MnistCNNModel()
n_iters = 1
num_epochs = 1

criterion = nn.CrossEntropyLoss()
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for i, (images, labels) in enumerate(custom_dataset_loader):
    images = Variable(images)
    labels = Variable(labels)
    # Clear gradients w.r.t. parameters
    optimizer.zero_grad()
    # Forward pass to get output/logits
    outputs = model(images)
    # Calculate Loss: softmax --> cross entropy loss
    loss = criterion(outputs, labels)
    # Getting gradients w.r.t. parameters
    loss.backward()
    # Updating parameters
    optimizer.step()

    break