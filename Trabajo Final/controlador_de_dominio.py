import samba
import samba.samba_tool

# Configura el nombre del dominio
domain_name = "example.com"

# Configura el nombre del controlador de dominio
dc_name = "dc1"

# Configura el nombre de usuario del administrador
admin_username = "administrator"


# Configura la ruta del archivo de registro
log_file = "/path/to/log/file.log"

# Crea una función para registrar el inicio de sesión de un usuario
def log_login(username):
    with open(log_file, "a") as f:
        f.write("Usuario {} inició sesión.\n".format(username))

# Inicia el controlador de dominio
samba.samba_tool.main(["domain", "provision"])

# Registra el inicio de sesión de un usuario de ejemplo
log_login("usuario_de_ejemplo")