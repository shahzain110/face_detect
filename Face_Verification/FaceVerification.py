from deepface import DeepFace
from Detection.functions import names
from Detection.AI_model import models, getFeatureMap, threshold,RecogAlgo
from Detection.functions import dbImagePath

# image and index will come to be verified
def faceVer_cus(file_path ,id):
    id_to_index = names.index(id)
    # img2 = f"{dbImagePath}{id_to_index}.jpg"
    fm_get = getFeatureMap(file_path)
    result = RecogAlgo(id_to_index,fm_get)
    print(f"Face Ver : {result}")
    if result < threshold:
        return "TRUE"
    else:
        return "False"

def faceVer_pre(file_path, id):
    try:
        id_to_index = names.index(id)
    except:
        return "Name To Index Failed"
    try:
        result = DeepFace.verify(img1_path = file_path, img2_path = f"{dbImagePath}{id_to_index}.jpg", model_name = models[2])
    except Exception as e:
        return f"No Face Found + {e}"
    return result['verified']