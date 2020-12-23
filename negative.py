#important library to show the image 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#importing numpy to work with large set of data.
import numpy as np
#image read function
img=mpimg.imread('E:\ImageProcessing\lena.png')
#image sclicing into 2D. 
x=img[:,:,0]
# x co-ordinate denotation. 
plt.xlabel("Value")
# y co-ordinate denotation.
plt.ylabel("pixels Frequency")
# title of an image .
plt.title("Original Image")
# imshow function with comperision of gray level value.
plt.imshow(x,cmap="gray")
#plot the image on a plane.
plt.show()
y=np.shape(x)
z=np.zeros(y)
#convert the image into its negative value.
z=255-x
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
plt.title("Negative image ")
plt.imshow(z,cmap="gray")
plt.show()