import numpy as np
import cv2
 
# load the image
image = cv2.imread('./2019-06-26-174012.jpg')

boundaries = [
	([160, 107, 56], [255, 203, 151]),
	([0, 163, 161], [108, 255, 255]),
	([126, 123, 118], [238, 235, 240])
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
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# show the images
cv2.imshow("images", image)
cv2.waitKey(0)

# cv2.imshow("images", output2)
# cv2.waitKey(0)

cv2.imshow("images", blackAndWhiteImage)
cv2.waitKey(0)

# 86, 467
# 366, 63


# source = to_index(86, 467)
# target = to_index(366, 63)


