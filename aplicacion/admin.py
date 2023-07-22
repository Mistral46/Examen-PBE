from django.contrib import admin
from aplicacion.models import Usuario,Topico,Post

# Register your models here.
#admin.site.register(Usuario)
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','password')
@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('deportes','noticias')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id_usuario','fecha', 'texto')
