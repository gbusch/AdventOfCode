import numpy as np
import matplotlib.pyplot as plt


def count_digits_per_layer(image_array):
    """
    >>> count_digits_per_layer([np.array([[1, 1]]), np.array([[3, 4]]), np.array([[5, 5]])])
    [Counter({1: 2}), Counter({3: 1, 4: 1}), Counter({5: 2})]
    """
    from collections import Counter
    return [Counter(layer.flatten()) for layer in image_array]


def get_color(image_slice):
    """
    >>> get_color(np.array([0, 1, 2, 0]))
    0
    >>> get_color(np.array([2, 1, 2, 0]))
    1
    >>> get_color(np.array([2, 2, 1, 0]))
    1
    >>> get_color(np.array([2, 2, 2, 0]))
    0
    >>> get_color(np.array([2, 2, 2, 2]))
    2
    """
    if image_slice[0] in [0, 1]:
        return image_slice[0]
    else:
        try:
            return get_color(image_slice[1:])
        except IndexError:
            return 2


def decode_image(image):
    decoded = np.ndarray((image.shape[1], image.shape[2]))
    for x in range(image.shape[2]):
        for y in range(image.shape[1]):
            decoded[y, x] = get_color(image[:, y, x])
    return decoded


if __name__ == "__main__":
    with open("./data/day08.txt") as f:
        data = np.array([int(i) for i in f.read()])

    image = data.reshape(-1, 6, 25)
    image_counts = count_digits_per_layer(image)
    image_counts_min0 = sorted(image_counts, key=lambda x: x.get(0))[0]

    print('PART ONE')
    print(image_counts_min0.get(1) * image_counts_min0.get(2))

    print('PART TWO')
    decoded_image = decode_image(image)

    plt.imshow(decoded_image)
    plt.show()
