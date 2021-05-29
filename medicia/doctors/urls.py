from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.doc_show),
    path('assistants/', views.asst_show),
    path('patients/', views.patient_show)
]
