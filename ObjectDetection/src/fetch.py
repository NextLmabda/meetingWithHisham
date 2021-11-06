import numpy as np
import selectivesearch


def extract_candidates(img):
    '''
    This function takes image as input, fetches the region proposals from an image
    :param img:
    :return:
    '''

    print('fetching the candidate regions within the image >>>>>>')
    img_lbl, regions = selectivesearch.selective_search(img, scale=200, min_size=100)
    img_area = np.prod(img.shape[:2]) # calculate the image area
    candidates = []

    # Fetch only those candidates(regions) that are over 5% of the total image area
        # and less than or equal to 100% of the image area
    for r in regions:
        if r['rect'] in candidates: continue
        if r['size'] < (0.05 * img_area): continue
        if r['size'] > (1 * img_area): continue
        x, y, w, h = r['rect']
        candidates.append(list(r['rect']))

    return candidates


