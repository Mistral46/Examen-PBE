from django.urls import path
from . import views

urlpatterns=[
    path('getUsuario/',views.getUsuario),
    path('getTopico/',views.getTopico),
    path('getPost/',views.getPost),
    path('postUsuario/',views.postUsuario),
    path('postTopico/',views.postTopico),
    path('postPost/',views.postPost),
    path('putUsuario/',views.putUsuario),
    path('putTopico/',views.putTopico),
    path('putPost/',views.putPost),
    path('deleteUsuario/',views.deleteUsuario),
    path('deleteTopico/',views.deleteTopico),
    path('deletePost/',views.deletePost),
]