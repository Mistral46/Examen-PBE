#from django.shortcuts import render
from aplicacion.models import Usuario,Topico,Post
from aplicacion.serializer import UsuarioSerializer,TopicoSerializer,PostSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
#Listar datos ////////////////////////////////////////////////
@api_view(['GET']) # Decorador para definir el metodo http 
def getUsuario(request):
    usuario = Usuario.objects.all()
    serializer = UsuarioSerializer(usuario,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getTopico(request):
    topico = Topico.objects.all()
    serializer = TopicoSerializer(topico,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getPost(request):
    post = Post.objects.all()
    serializer = PostSerializer(post,many=True)
    return Response(serializer.data)

#Crear Datos////////////////////////////////////////////
@api_view(['POST'])
def postUsuario(request):
    data = request.data
    usuario = Usuario.objects.create(
        nombre = data['nombre'],
        email = data['email'],
        password = data['password'],
    )
    serializer = UsuarioSerializer(usuario,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def postTopico(request):
    data = request.data
    topico = Topico.objects.create(
        deportes = data['deportes'],
        noticias = data['noticias'],
    )
    serializer = TopicoSerializer(topico,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def postPost(request):
    data = request.data
    post = Post.objects.create(
        id_usuario = data['id_usuario'],
        fecha = data['fecha'],
        texto = data['texto']
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

#Actualizacion de Datos//////////////////////////////////////////
@api_view(['PUT'])
def putUsuario(request):
    data = request.data
    usuario = Usuario.objects.get(id = data['id'])
    serializer = UsuarioSerializer (instance = usuario, data=data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def putTopico(request):
    data = request.data
    topico = Topico.objects.get(id = data['id'])
    serializer = TopicoSerializer(instance = topico, data = data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def putPost(request):
    data = request.data
    post = Post.objects.get(id = data['id'])
    serializer = PostSerializer( instance = post, data = data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#Borrar datos //////////////////////////////////////////
@api_view(['DELETE'])
def deleteUsuario(request):       
    data = request.data
    usuario = Usuario.objects.filter(id = data['id'])
    usuario.delete()
    respuesta ={'message':'Elemento Eliminado'}
    return Response(respuesta,status = status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deleteTopico(request):
    data = request.data
    topic=Topico.objects.filter(id=data['id'])
    topic.delete()
    respuesta = {'message':'Elemento Eliminado'}
    return  Response(respuesta , status = status.HTTP_204_NO_CONTENT)
@api_view(['DELETE'])
def deletePost(request):
    data = request.data
    post=Post.objects.filter(id=data['id'])
    post.delete()
    respuesta={'message': 'Elemento eliminado' }
    return   Response(respuesta , status = status.HTTP_204_NO_CONTENT)
