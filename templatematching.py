import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('magangsendiri.jpg', 0)
img2 = img.copy()
template = cv2.imread('magang.jpg', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (15, 15)

for met in methods:
    img = img2.copy()
    method = eval(met)
    # menggunakan template matching
    res = cv2.matchTemplate(img, template, method)

    # mencari ukuran citra template untuk menggambar kotak
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # metode TM_SQDIFF dan TM_SQDIFF_NORMED menggunakan persamaan yang sedikit berbeda
    # sehingga dibuatkan fungsi khusus untuk mengambil nilai minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

# buat persegi pada lokasi yang ditemukan
    # 2 adalah ketebalan garis kotak
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    print("hasil metode", met, ": ")
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Hasil matching'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Lokasi terdeteksi'), plt.xticks([]), plt.yticks([])
    plt.show()
