import os
import cv2
import requests
import numpy as np

'''Get User Details'''
eid=int(input('Enter User ID : '))
Firstname=input('Enter User Firstname : ')
Lastname=input('Enter User Lastname : ')
Gender=input('Enter User Gender [M: Male | F: Female] : ')

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

# url from IP cam
# http://<ip-addr>:<port>/shot.jpg is from ip cam
url='http://192.168.1.102:8080/shot.jpg' 
i=0
while True:
    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    image = cv2.imdecode(img_arr,-1)

    cv2.imshow(Firstname, image)

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