from typing import Dict

from torchvision import transforms

from base import BaseDataLoader
from datasets.dataset_2d import CustomDataset2D


class CustomDataLoader(BaseDataLoader):

    def __init__(self, dataset_args: Dict, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        self.data_dir = data_dir
        # self.dataset = datasets.MNIST(self.data_dir, train=training, download=True, transform=trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)

    def _init_dataset(self):
        pass










