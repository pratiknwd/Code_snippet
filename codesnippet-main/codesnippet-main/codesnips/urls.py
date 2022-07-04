from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path('view/<int:pk>',views.viewData, name='viewData'),
     path('delete/<int:pk>',views.deleteData, name='deleteData'),
     path('edit/<int:pk>',views.edit, name='edit')
]