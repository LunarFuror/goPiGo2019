# Note for Jim:  In MacOS Run this command "workon OpenCV-master-py3" - select virtualenv as Python interrpretor
import numpy as np
import cv2
 
# load the image
image = cv2.imread('./JustBoard1.jpg')

boundaries = [
	([160, 107, 56], [255, 203, 151]),
	([0, 163, 161], [163, 255, 255]),
	([116, 113, 108], [248, 245, 250])
]

	# rgb([148, 145, 140], [168, 165, 160])

output2 = None
firstImageSkipped = False

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	if firstImageSkipped == True:
		if output2 is None:
			output2 = output
		else:
			output2 = cv2.bitwise_or(output2, output)
	else:
		firstImageSkipped = True

# Convert to black and White
grayImage = cv2.cvtColor(output2, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)

# show the images
cv2.imshow("images", image)
cv2.waitKey(0)

cv2.imshow("images", output2)
cv2.waitKey(0)

cv2.imshow("images", grayImage)
cv2.waitKey(0)

cv2.imshow("images", blackAndWhiteImage)
cv2.waitKey(0)

# ? ? ? ? ? ?  
# ? [181, 470], [102, 374], [36. 301], [5, 239], ?
# ? [453, 479], [322, 395], [234, 319], [161, 260], [102, 210], [51, 168]
# ?, [545, 420], [432, 341], [342, 277], [266, 226], [202, 182], [150, 143]
# ?, [632, 362], [524, 297], [431, 242], [354, 197], [286, 159], [231, 128]
# ?, ?, [596, 261], [502, 211], [425, 174], [359, 140], [304, 111]
# ?, ?, ?, [565, 188], [489, 155], [420, 123], [364, 98]
# ?, ?, ?, [620, 166], [540, 135], [475, 108], [424, 82]


# source = to_index(86, 467)
# target = to_index(366, 63)


