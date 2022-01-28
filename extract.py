import os
import pdb
from collections import defaultdict

import torch
import torchvision
from torchvision.datasets.folder import default_loader


def to_arr(images: torch.tensor) -> torch.tensor:
    s = 384
    p = 2
    return [images[:, i * (s + p) + p:i * (s + p) + p + s, p:-p] for i in range(8)]


def generate():
    to_tensor = torchvision.transforms.ToTensor()
    for l in range(8, 12):
        for name in ['key', 'query', 'value']:
            images = to_tensor(default_loader(os.path.join('blogs', 'low', 'vis', name, f'{l}.png')))
            images = to_arr(images)
            for f in range(8):
                torchvision.utils.save_image(images[f], os.path.join('blogs', 'low', 'vis', name, f'{l}_{f}.png'))

    for l in range(0, 2):
        for name in ['key', 'query', 'value']:
            images = to_tensor(default_loader(os.path.join('blogs', 'low', 'vis', name, f'{l}.png')))
            images = to_arr(images)
            for f in range(8):
                torchvision.utils.save_image(images[f], os.path.join('blogs', 'low', 'vis', name, f'{l}_{f}.png'))


if __name__ == '__main__':
    generate()
