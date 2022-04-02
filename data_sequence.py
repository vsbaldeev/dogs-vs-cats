import tensorflow as tf
import skimage.io as io
import numpy as np


class DogCatSequence(tf.keras.utils.Sequence):
    def __init__(self, files_list, batch_size):
        if batch_size > len(files_list):
            raise ValueError('Batch size is bigger than length of files list')
        self._files_list = files_list
        self._batch_size = batch_size

    def __getitem__(self, index):
        end = min((index + 1) * self._batch_size, len(self._files_list) - 1)
        batch_files_list = self._files_list[index * self._batch_size: end]

        batch_x = np.array([io.imread(filename) for filename in batch_files_list])
        batch_y = np.array([float(filename.startswith('dog')) for filename in batch_files_list])

        return batch_x, batch_y

    def __len__(self):
        return np.ceil(len(self._files_list) / self._batch_size)