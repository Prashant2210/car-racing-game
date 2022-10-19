from email.mime import image
from PIL import Image
img_PIL=image.open('backgroung1.jpg')
img_PIL.show()
from IPython.display import display
from PIL import Image
img_PIL=image.open('background1.jpg')
display(img_PIL)

img_PIL.save('baackground1.png')

import  cv2
image_cv2=cv2.imread('background1.png')
cv2.imshow("Background image ")