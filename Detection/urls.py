from django.urls import path
from Detection import views

# url config
urlpatterns = [
    path('faceVer_cus/' , views.faceVer_cus),
    path('faceVer_pre/' , views.faceVer_pre),
    path('faceRecog_cus/' , views.faceRecog_cus),
    path('faceRecog_pre/' , views.faceRecog_pre),
    
]