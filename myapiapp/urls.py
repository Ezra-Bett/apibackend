# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet, UserRegistrationViewSet
# router = DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('register', UserRegistrationViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api/', include('products.urls')),
# ]

from django.urls import path, include
from rest_framework import routers
from myapiapp.views import PatientViewSet

router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]