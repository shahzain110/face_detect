from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
# from keras_preprocessing.image import load_img
# from tensorflow.keras.utils import img_to_array
import numpy as np
from keras.models import Model
from numpy import expand_dims
from scipy import spatial
from sklearn.metrics import pairwise
from deepface import DeepFace
from PIL import Image as im
# from scipy.misc import toimage


global threshold
threshold = 1.4

models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]

backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe'
]

# Inception Model
def getFeatureMap(img1, img2):
    face1 = DeepFace.detectFace(img_path = img1, 
        target_size = (299, 299),
        detector_backend = backends[4])

    face2 = DeepFace.detectFace(img_path = img2, 
    target_size = (299, 299),
    detector_backend = backends[4])
      
    model = InceptionV3()
    model = Model(inputs=model.inputs, outputs=model.layers[1].output)
    # model.summary()
    # img = load_img(img1, target_size=(299, 299))
    # img = img_to_array(img)
    img = expand_dims(face1, axis=0)
    img = preprocess_input(img)
    feature_maps_1 = model.predict(img)

    # img = load_img(img2, target_size=(299, 299))
    # img = img_to_array(img)
    img = expand_dims(face2, axis=0)
    img = preprocess_input(img)
    feature_maps_2 = model.predict(img)
    # res = np.allclose(feature_maps_1,feature_maps_2)
    # print(feature_maps_1)
    # print(feature_maps_2)
    result = np.linalg.norm(feature_maps_1 - feature_maps_2)
    # dataSetI = feature_maps_1.ravel()
    # dataSetII = feature_maps_2.ravel()
    # result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
    return result
    