from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
import numpy as np
from keras.models import Model
from numpy import expand_dims
from scipy import spatial
# from sklearn.metrics import pairwise
from deepface import DeepFace
# from PIL import Image as im
# from scipy.misc import toimage
from numpy.linalg import norm
import pickle
from Detection.functions import dbImagePath, names

global threshold
threshold = 0.5
model = InceptionV3()
print("MODEL LOADED")      
model = Model(inputs=model.inputs, outputs=model.layers[1].output)

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

def gen_fmPickle():
  try:
    print("Generating Pickles Now >>>")
    pickle_dict = {}
    for x in range(0,len(names)):
      img = dbImagePath + f'{x}.jpg'
      featureMap = getFeatureMap(img)
      pickle_dict[x] = featureMap
    # print(pickle_dict)
    filename = dbImagePath + 'dbImages'
    outfile = open(filename,'wb')
    pickle.dump(pickle_dict,outfile)
    outfile.close()
  except Exception as e:
    return f"Error While Generating Pickle : {e}"

# Inception Model
def getFeatureMap(image):
    try:
      face = DeepFace.detectFace(img_path = image, target_size = (299, 299),detector_backend = backends[4])
    except Exception as e:
      return f"NO FACE FOUND : {e}"
    
    try:
      img = expand_dims(face, axis=0)
      img = preprocess_input(img)
      feature_map = model.predict(img)
      # print(feature_map.shape)
    except Exception as e:
      return f"Error while extracing Feature Maps : {e}"
    return feature_map
    
def RecogAlgo(index,img2Features):
  filename = dbImagePath + 'dbImages'
  infile = open(filename,'rb')
  featureMaps = pickle.load(infile)
  infile.close()

  # dataSetI = featureMaps[index].ravel()
  # dataSetII = img2Features.ravel()
  # result = (1 - spatial.distance.cosine(dataSetI, dataSetII))*0.5
  
  result = np.allclose(featureMaps[index],img2Features)
  
  # Cosine Similarity
  # A  = featureMaps[1].reshape(-1, 149, 149)
  # B = img2Features.reshape(-1, 149, 149)
  # result = np.dot(A,B)/(norm(A)*norm(B))


  print(result)
  return result
    
gen_fmPickle()
# LT normaliztaion
# extract every feature bofore