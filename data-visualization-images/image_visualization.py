import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import cv  #-->install it

#READING IMAGE USING MATPLOTLIB
img=mpimg.imread('D:/File Manager/DATA SCIENCE/Data Visualization/1000061498.jpg')
plt.imshow(img)
plt.show()

#READING IMAGE USING OpenCV
#imgcv2=cv2.imread('D:/File Manager/DATA SCIENCE/Data Visualization/1000061498.jpg')   #needs to be converted  bgr to rgb
#plt.imshow(imgcv2)
#plt.show()

#imgcv2=cv2.cvtColor(imgcv2,cv2.COLOR_BGR2RGB)
#plt.imgshow(imgcv2)
#plt.show()

#CHANGING ASPECT--->height and width
plt.imshow(img,aspect=0.5)    
plt.show()

#MULTIPLE IMAGES
img1=mpimg.imread('D:/File Manager/DATA SCIENCE/Data Visualization/505.jpg')
img2=mpimg.imread('D:/File Manager/DATA SCIENCE/Data Visualization/1000015820.jpg')
img3=mpimg.imread('D:/File Manager/DATA SCIENCE/Data Visualization/1000061498.jpg')

plt.figure()
plt.subplot(2,2,1)
plt.imshow(img1)
plt.subplot(2,2,2)
plt.imshow(img2)
plt.subplot(2,2,3)
plt.imshow(img3)
plt.show()

#COLOR BAR
plt.imshow(img,aspect=1.5,cmap='magma')
plt.colorbar()
plt.show()

#SAVING OUTPUT TO THE STORAGE
plt.savefig('D:/File Manager/DATA SCIENCE/Data Visualization/subplot.png',quality=100,facecolor='k')  #wroeks in goggle colab
plt.show()

