from Login_App.models import Usuarios
from  Login_App.serializer import UsuariosSerializer
class LoginController:
    def __init__(self):
        self.usuarios = Usuarios.objects.all()

    def listarUsuarios(self):
        try:
            serializer = UsuariosSerializer(self.usuarios, many=True)
            usuarios = serializer.data
            return usuarios
        except Exception as e:
            return f'Error: {str(e)}'