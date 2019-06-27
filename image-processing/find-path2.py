from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                # eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 255
                # eachPix[3] = 255
    return newAr



i = Image.open('./2019-06-26-174012.jpg')
iar = np.asarray(i)
iar_copy = iar.copy()
iar_copy = threshold(iar_copy)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar_copy)
ax2.imshow(i)
plt.show()