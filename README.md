# CaptureCropPhoto
[site](https://ajinkz.github.io/CaptureCropPhoto/)

A simple python code useful in Face Recognition for data collection to capture photo using webcam and crop to image centered to face detected

## Prerequisites

- Python 3.6.x
- OpenCV 4.0.0 (pip install opencv-contrib-python) 
- Autocrop library (pip install autocrop)

## Execution

`python CaptureCropPhoto.py`

## Working

- It will ask to enter user first name, last name, id, gender,etc
- Then it will create a directory with the same and cv2 session will start
- Press '**c**' to capture photo.Press as many times as the number of photos of user you want
- Press '**s**' to autocrop all photos in that directory to face region
- Press '**x**' to break & exit
- Directory name will be in format
  `<Id.no>_<First name>_<Last name>_<Gender M/F>`
  e.g. `007_James_Bond_M`
- Directory structure will like this
 
 ```
 ├───007_James_Bond_M
      └───007_James_Bond_M0.jpg
      └───007_James_Bond_M1.jpg
      └───007_James_Bond_M2.jpg
      .
      .
      .
```

## Acknowledgements
- [François Leblanc](https://medium.com/@manivannan_data/keyboard-control-for-save-image-and-destroywindow-in-opencv-335c084fe742)
- [Manivannan Murugavel](https://github.com/leblancfg/autocrop)

