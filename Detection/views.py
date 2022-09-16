from django.http import JsonResponse
from Face_Recognition.FaceRecognization import faceRecog_pre as frp
from Face_Recognition.FaceRecognization import faceRecog_cus as frc
from Face_Verification.FaceVerification import faceVer_pre as fvp
from Face_Verification.FaceVerification import faceVer_cus as fvc
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def faceVer_cus(request):
    try:
        id = request.POST.get("name")
        file_path = 'Detection/UserSavedImg/0.jpg'
        img_01 = request.FILES['file'].read()
        downloadFile(file_path, img_01)
        res = fvc(id)
    except Exception as e:
        res = "NO MATCH"
        print("EXCEPTIION : ")
        print(e)
    mydict = {'Face Verification' : res}
    return JsonResponse(mydict)


@csrf_exempt
def faceRecog_cus(request):
    try:
        file_path = 'Detection/UserSavedImg/0.jpg'
        img_01 = request.FILES['file'].read()
        downloadFile(file_path, img_01)
        res = frc()
    except Exception as e:
        res = "NO MATCH"
        print("EXCEPTIION : ")
        print(e)
    mydict = {'Face Verification' : res}
    return JsonResponse(mydict)

# Image and Index will be given
@csrf_exempt
def faceVer_pre(request):
    try:
        id = request.POST.get("name")
        file_path = 'Detection/UserSavedImg/0.jpg'
        img_01 = request.FILES['file'].read()
        downloadFile(file_path, img_01)
        res = fvp(id)
    except Exception as e:
        print("EXCEPTION:")
        print(e)
    
    mydict = {'Face Verification' : res}
    return JsonResponse(mydict)


# Image will INPUT and Index Will be Output
@csrf_exempt
def faceRecog_pre(request):
    try:
        file_path = 'Detection/UserSavedImg/0.jpg'
        img_01 = request.FILES['file'].read()
        downloadFile(file_path, img_01)
        res = frp()
    except Exception as e:
        res = "NO MATCH"
        print("EXCEPTIION : ")
        print(e)
    mydict = {'Face Verification RESULTS' : res}
    return JsonResponse(mydict)

# for downloading image
def downloadFile(file_path, img_01):
    f = open(file_path, 'wb')
    f.write(img_01)
    f.close()