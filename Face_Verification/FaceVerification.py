from deepface import DeepFace
from Detection.functions import names
from Detection.AI_model import models, getFeatureMap, threshold

# image and index will

def faceVer_cus(id):
    imagePath = 'Detection/UserSavedImg/0.jpg'
    id_to_index = names.index(id)
    print(id_to_index)
    img2 = f"Detection/savedImages/{id_to_index}.jpg"
    result = getFeatureMap(imagePath,img2)
    print(f"Face Ver : {result}")
    if result < threshold:
        return "TRUE"

def faceVer_pre(id):
    imagePath = 'Detection/UserSavedImg/0.jpg'
    id_to_index = names.index(id)
    print(id_to_index)
    result = DeepFace.verify(img1_path = imagePath, img2_path = f"Detection/savedImages/{id_to_index}.jpg", model_name = models[2])
    return result['verified']