from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    # path('details/',views.details,name='details'),
    path('<slug:slug>/',views.details,name='details')
]