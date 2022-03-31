import os
import argparse
import numpy as np
from skimage.transform import resize
from skimage.io import imread, imsave


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_folder', type=str, required=True)
    parser.add_argument('--output_folder', type=str, required=True)
    parser.add_argument('--output_height', type=int, required=True)
    parser.add_argument('--output_width', type=int, required=True)

    return parser.parse_args()


def resize_image(image, height, width):
    resized_image = resize(image, (height, width), anti_aliasing=True)
    resized_image = np.round(resized_image * 255.0).astype(np.uint8)
    return resized_image


if __name__ == '__main__':
    args = get_args()
    files_list = os.listdir(args.input_folder)
    for filename in files_list:
        print(filename)
        image = imread(os.path.join(args.input_folder, filename))
        resized_image = resize_image(image, args.output_height, args.output_width)
        imsave(os.path.join(args.output_folder, filename), resized_image)