# Importar la base de datos
 # la variable usuarios de mi bd estará disponible en este archivo.
from datetime import*
from bd import*
# crear clase para usuario. Esta clase tendrá los siguientes metodos

# Actualizar la edad del usuario.
# Verificar si el usuario esta registrado o existe en este registro.
# Validar usuario y password.
class Usuario:
    def __init__(self, DNI, Nombre, F_nacimiento, Edad, Usuario, Password):
        self.DNI = DNI
        self.Nombre = Nombre
        self.F_nacimiento = F_nacimiento
        self.Edad = Edad
        self.Usuario = Usuario
        self.Password = Password

    def mostrar_usuario(self, ide):
        resultado = list(filter(lambda par: par['DNI'] == ide, usuarios))
        return f'''Aquí tienes los datos del usuario que buscaste:
        {resultado}'''

    def agregar_edad(self, clave, valor):
        for usuario in usuarios:
            if usuario['DNI'] == self.DNI:
                usuario[clave] = valor
                return 'Se actualizó.'
        return 'Usuario no encontrado.'

    def verificar_usuario(self, usuario_buscar):
        for usuario in usuarios:
            if usuario['Usuario'] == usuario_buscar:
                return 'Usuario registrado.'
        return 'Usuario no encontrado en los registros.'

    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuarios:
            if usuario['Usuario'] == usuario_a_validar and usuario['Password'] == password_a_validar:
                return 'Usuario y contraseña válidos.'
        return 'Usuario o contraseña incorrectos.'

    def actualizar_usuario(self, DNI, Nombre, F_nacimiento, Edad, Usuario, Password):
        for usuario in usuarios:
            if usuario['DNI'] == self.DNI:
                usuario['Nombre'] = Nombre
                usuario['F_nacimiento'] = F_nacimiento
                usuario['Edad'] = Edad
                usuario['Usuario'] = Usuario
                usuario['Password'] = Password
                return 'Usuario actualizado.'
        return 'Usuario no encontrado.'


actu = Usuario(74484162, "Adan", "10/12/2003", None, "AHC", "0717")
print(actu.agregar_edad("edad", 20))
print(actu.mostrar_usuario(74484162))
usuario_a_buscar = "AHC"
print(actu.verificar_usuario(usuario_a_buscar))
print(actu.mostrar_usuario(74484162))
usuario_a_validar = "AHC"
password_a_validar = "0717"
print(actu.validar_usuario_password(usuario_a_validar, password_a_validar))
print(actu.mostrar_usuario(74484162))

# Actualizar usuario
actu.actualizar_usuario(74484162, "Adán", "10/12/2003", 20, "AHC", "0717")
print(actu.mostrar_usuario(74484162))