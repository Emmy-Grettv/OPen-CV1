# import cv2

# image = cv2.imread('assignment-001-given.jpg')
# cv2.rectangle(image, (265, 920),(990,195), (0,255,0),5 )
# cv2.putText(image, 'RAH972U', (890, 175), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
# cv2.imshow('Image Window', image)
# cv2.waitKey(0)

# cv2.imwrite("assignment-001-result.jpg", image)

# cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread('assignment-001-given.jpg')
cv2.rectangle(image, (265, 920), (990, 195), (0, 255, 0), 5)

text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 4
text_color = (0, 255, 0)  
text_x, text_y = 885, 170

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
rect_start = (text_x - 1, text_y - text_height - 11)  
rect_end = (text_x + text_width + 0, text_y + baseline + 1)  

overlay = image.copy()
cv2.rectangle(overlay, rect_start, rect_end, (0, 0, 0), -1)  

alpha = 0.4  
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

cv2.imshow('Annotated Image', image)
cv2.waitKey(0)

cv2.imwrite("assignment-001-result.jpg", image)

cv2.destroyAllWindows()
