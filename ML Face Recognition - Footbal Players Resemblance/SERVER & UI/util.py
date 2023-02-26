import json
import joblib
import numpy as np
import cv2
import base64
import pywt
import matplotlib.pyplot as plt
__class_name_to_number = {}
__class_number_to_name = {}
__model = None

def classify_image(image_base64_data = None, file_path = None):
    imgs = get_cropped_image_if_2_eyes(image_base64_data, file_path)
    result = []
    for img in imgs:
        scaled_img = cv2.resize(img, (32, 32))
        img_haar =w2d(img, 'db1', 5)
        img_haar_scaled = cv2.resize(img_haar, (32,32))
        combined_img = np.vstack((scaled_img.reshape(32*32*3, 1), img_haar_scaled.reshape(32*32*1, 1)))
        final = combined_img.reshape(1, 32*32*3+32*32).astype(float)
        result.append({
             'Player_name' : __class_number_to_name[__model.predict(final)[0]],
             'Similarity' : str(np.max(np.round(__model.predict_proba(final)[0]*100, 2))) + ' %',
             'Player_class_number' : int(__model.predict(final)[0])
        })
    return result

def load_saved_artifacts():
    print ('Loading artifacts -- START --')
    global __class_number_to_name
    global __class_name_to_number
    with open ('./Server/artifacts/class_dictionary.json', 'r') as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k, v in __class_name_to_number.items()}
    global __model
    if __model == None:
        with open ('./Server/artifacts//saved_model.pk1', 'rb') as f:
            __model = joblib.load (f)
    print ('Loading artifacts -- DONE --')

def get_cv2_image_from_base64_string (image_base64_data):
    encoded_data = image_base64_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_cropped_image_if_2_eyes(image_base64_data, file_path):
    face_cascade = cv2.CascadeClassifier('./Server/opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./Server/opencv/haarcascades/haarcascade_eye.xml')
    if file_path:
        img = cv2.imread(file_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cropped_faces = []
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    return cropped_faces

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)
    imArray /= 255;
    # compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)
    return imArray_H

def get_b64_test_image():
    with open("base64_2.txt") as f:
        return f.read()

if __name__ == '__main__':
   load_saved_artifacts()
   #print(classify_image(file_path='.\Server\lyes.jpg'))
   #print (classify_image(file_path='./test_image/88.png'))
   #print (classify_image(file_path='./test_image/788.jpg'))
   #print (classify_image(file_path='./test_image/784.jpg'))
   # print (classify_image(file_path='./test_image/897.jpg'))
   # print (classify_image(file_path='./test_image/8954.jpg'))
   # print (classify_image(file_path='./test_image/2879.jpg'))
   # print (classify_image(file_path='./test_image/0bf.jpg'))