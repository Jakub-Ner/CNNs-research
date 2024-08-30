import os
from PIL import Image
import itertools
import numpy as np
import matplotlib.pyplot as plt

def merge_imgs(paths: list[str]):
    imgs = [Image.open(path) for path in paths] 
    for file in paths:
        os.remove(file)
    widths, heights = zip(*(i.size for i in imgs))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in imgs:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    return new_im

def hist_image(img, ax, title=''):
  ax.hist(img[:, :, 0].flatten() * 255, color='red', bins=255)
  ax.hist(img[:, :, 1].flatten() * 255, color='green', bins=255)
  ax.hist(img[:, :, 2].flatten() * 255, color='blue', bins=255)
  ax.set_title(title)

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')