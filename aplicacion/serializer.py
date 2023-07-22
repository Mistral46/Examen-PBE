from rest_framework.serializers import ModelSerializer
from aplicacion.models import Usuario,Topico,Post

class UsuarioSerializer (ModelSerializer):
    class Meta:
        model = Usuario
        fields=['id','nombre','email','password']
class TopicoSerializer (ModelSerializer):
    class Meta:
        model = Topico
        fields =['id','deportes','noticias']
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['id','id_usuario','fecha','texto']        
