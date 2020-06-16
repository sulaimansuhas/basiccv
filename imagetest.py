from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
from statistics import mean
import time
def threshold (imageArray):
	balanceAr = []
	newAr = imageArray
	for row in imageArray:
		for pixel in row:
			avgNum = mean(pixel[:3])
			balanceAr.append(avgNum)
	balance = mean(balanceAr)
	for eachRow in newAr:
		for eachPix in eachRow:
			if(mean(eachPix[:3])>balance):
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
			else:
				eachPix[0]= 0
				eachPix[1]= 0
				eachPix[2]= 0
				eachPix[3]= 255
	return newAr


i = Image.open('images/numbers/0.1.png')
iar = threshold(np.array(i))
i2 = Image.open('images/numbers/y0.4.png')
iar2 = threshold(np.array(i2))
i3 = Image.open('images/numbers/y0.5.png')
iar3 = threshold(np.array(i3))
i4 = Image.open('images/sentdex.png')
iar4 = threshold(np.array(i4))

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()