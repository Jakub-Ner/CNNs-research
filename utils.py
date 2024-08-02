import os
from PIL import Image


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

