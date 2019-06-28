import numpy as np
import cv2
 
# load the image
image = cv2.imread('./2019-06-26-174012.jpg')

boundaries = [
	([160, 107, 56], [255, 203, 151]),
	([38, 201, 199], [88, 251, 249]),
	([138, 135, 130], [238, 235, 240])
]

	# rgb([148, 145, 140], [168, 165, 160])

output2 = None

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	if output2 is None:
	  output2 = output
	else:
		output2 = cv2.bitwise_or(output2, output)

	# show the images
	cv2.imshow("images", np.hstack([image, output2]))
	cv2.waitKey(0)