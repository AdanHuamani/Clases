# Importar la base de datos
from datetime import* # la variable usuarios de mi bd estará disponible en este archivo.
from bd import*
# crear clase para usuario. Esta clase tendrá los siguientes metodos

# Actualizar la edad del usuario.
# Verificar si el usuario esta registrado o existe en este registro.
# Validar usuario y password.
def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_nacimiento.month > fecha_actual.month or (fecha_nacimiento.month == fecha_actual.month and fecha_nacimiento.day > fecha_actual.day):
        edad -= 1
    return edad

for usuario in obt: 
    fecha_nacimiento = datetime.strptime(usuario["f_nacimiento"], "%d/%m/%Y")
    usuario["edad"] = calcular_edad(fecha_nacimiento)

print(obt)

dni_buscar= 12345678
print(any(u["dni"]==dni_buscar for u in obt))

dni_validar= 12345678
password_validar="query1234"
print(any(u["dni"]==dni_validar and ["password"]==password_validar for u in obt))