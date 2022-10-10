from django.http import JsonResponse
from Face_Recognition.FaceRecognization import faceRecog_pre as frp
from Face_Recognition.FaceRecognization import faceRecog_cus as frc
from Face_Verification.FaceVerification import faceVer_pre as fvp
from Face_Verification.FaceVerification import faceVer_cus as fvc
from django.views.decorators.csrf import csrf_exempt
import uuid
import os
from Detection.functions import downloadFile

global getImagesPath
getImagesPath = 'Detection/getImages/'

# Create your views here.
@csrf_exempt
def faceVer_cus(request):
    try:
        uid = uuid.uuid4()
        id = str(request.POST.get("name"))
        if id == 'None' or id == '':
            res = "Invalid Name"
            mydict = {'Face Verification Results' : res}
            return JsonResponse(mydict)

        file_path = getImagesPath + f'{uid}.jpg'
        
        try:
            img_01 = request.FILES['file'].read()
        except Exception as e:
            res = f"Invalid Filetype {e}"
            mydict = {'Face Verification Results' : res}
            return JsonResponse(mydict)
        
        if downloadFile(file_path, img_01):
            res = fvc(file_path,id)
            os.remove(file_path)
        else:
            return "Error Downloading Image"
            
    except Exception as e:
        res = f"An Error Occurred While Verifying Image {e}"
    mydict = {'Face Verification' : res}
    return JsonResponse(mydict)


@csrf_exempt
def faceRecog_cus(request):
    try:
        uid = uuid.uuid4()
        file_path = getImagesPath + f'{uid}.jpg'
        img_01 = request.FILES['file'].read()
        downloadFile(file_path, img_01)
        if downloadFile:
            res = frc()
            os.remove(file_path)
        else:
            return "Error Downloading Image"
    except Exception as e:
        os.remove(file_path)
        res = "An Error Occurred While Recognizing Image" + e
    mydict = {'Face Recognization' : res}
    return JsonResponse(mydict)

# Image and Index will be given
@csrf_exempt
def faceVer_pre(request):
    try:
        uid = uuid.uuid4()
        id = str(request.POST.get("name"))
        if id == 'None' or id == '':
            res = "Invalid Name"
            mydict = {'Face Verification Results' : res}
            return JsonResponse(mydict)

        file_path = getImagesPath + f'{uid}.jpg'
        
        try:
            img_01 = request.FILES['file'].read()
        except:
            res = "Invalid Filetype"
            mydict = {'Face Verification Results' : res}
            return JsonResponse(mydict)

        if downloadFile(file_path, img_01):
            res = fvp(file_path,id)
            os.remove(file_path)
        else:
            return "Error Downloading Image"
    except Exception as e:
        res = "An Error Occurred While Processing API" + e
    mydict = {'Face Verification Results' : res}
    return JsonResponse(mydict)


# Image will INPUT and Index Will be Output
@csrf_exempt
def faceRecog_pre(request):
    try:
        uid = uuid.uuid4()
        try:
            file_path = getImagesPath + f'{uid}.jpg'
            img_01 = request.FILES['file'].read()
        except:
            res = "Invalid Filetype"
            mydict = {'Face Verification Results' : res}
            return JsonResponse(mydict)

        if downloadFile(file_path, img_01):
            try:
                res = frp(file_path)
            except Exception as e:
                res = "Error while Recognization"
            os.remove(file_path)
        else:
            return "Error Downloading Image"
    except Exception as e:
        res = "Error While API Processing The Request"
    mydict = {'Face Recognization RESULTS' : res}
    return JsonResponse(mydict)