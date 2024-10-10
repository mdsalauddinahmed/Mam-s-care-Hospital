from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router = DefaultRouter()
router.register('specialization',views.SpecializationVewSet)
router.register('Designation',views.DesignationVewSet)
router.register('AvailaleTime',views.AvailaleTimeVewSet)
router.register('Doctor',views.DoctorVewSet)
router.register('Review',views.ReviewVewSet)
 
urlpatterns = [
    path('',include(router.urls)),
   
]