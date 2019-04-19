'''
Requires:
Python==3.6.x
pip install opencv-contrib-python
pip install autocrop
'''
import os
import cv2

'''Get User Details'''
eid=int(input('Enter User ID : '))
Firstname=input('Enter User Firstname : ')
Lastname=input('Enter User Lastname : ')
Gender=input('Enter User Gender [M: Male | F: Female]\n')

name=str(eid)+'_'+Firstname+'_'+Lastname+'_'+Gender
# print(name)

'''create Directory with user name'''
cwd=os.getcwd()
folder=os.path.join(cwd,name)
# print(folder)

try:  
    os.mkdir(folder,0o777)
except OSError:  
    print ("Creation of the directory %s failed" % folder)
else:  
    print ("Successfully created the directory %s" % folder)

'''Capture Photos using webcam'''
# 0 for build-in camera, 1 for USB camera. Incase no built-in camera, usb camera becomes Primary
camera = cv2.VideoCapture(0) 
i=0
while True:
	return_value, image = camera.read()
	image = cv2.flip(image,180) # Mirror like effect
	cv2.imshow(name,image)

	k = cv2.waitKey(1)

	if k == ord('c'): # wait for 's' key to save and exit
		'''capture the frame and write it on to disk into jpg/png format'''
		cv2.imwrite(os.path.join(folder ,name+str(i)+'.jpg'), image)
		i+=1
	elif k== ord('s'):
		'''Autocropping the capture pictures'''
		myCmd = 'autocrop -i '+name+' -o '+name+' --no-confirm'
		try:  
			os.system(myCmd)	
		except OSError:  
			print ("Cropped photos %s failed" % name)
		else:  
			print ("Successfully Cropped photos %s" % name)
	elif k== ord('x'): #Exit
		break
		# cv2.destroyAllWindows()