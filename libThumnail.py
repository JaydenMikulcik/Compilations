import sys
import os
import cv2
import tensorflow as tf
from PIL import Image





MOVIE_PATH = r'C:\Users\jjmik\Videos\CompilationVideos\final_comp.mp4'


def create_thumb():
    if not os.path.exists(MOVIE_PATH):
        return
        
    #TODO 3 images to concat below
    #cap = cv2.VideoCapture('final_comp.mp4')
    #ret, frame = cap.read()
    

    images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save('final_thumb.jpg')

if __name__ == '__main__':
    create_thumb()

