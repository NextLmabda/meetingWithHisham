
from torch_snippets import *
#import cv2
import selectivesearch
from skimage.segmentation import felzenszwalb

from src.fetch import extract_candidates

# Leveraging SelectiveSearch to generate Region Proposals

img = read('img2.jpg', 1)
'''
segments_fz = felzenszwalb(img, scale=200)

subplots([img, segments_fz], titles=['Original Image', 'Image Post\nfelzenszwalb segmentation'],
         sz=10, nc=2)
'''

candidates = extract_candidates(img)
show(img, bbs=candidates)