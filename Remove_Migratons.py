import os
import sys
from distutils.util import strtobool

# Cambiar el valor de acuerdo a la configuración de tu proyecto.
APPS_FOLDER = "C:/Users/VLLS SISTEMAS III/Documents/ProyectoCIM/PROYECTO_CIM"  # <- Ruta de nuestra carpeta contenedora de apps


# Obtenemos la ruta de nuestro archivo.
BASE_DIR = os.getcwd()
# Ruta completa para iniciar el proceso de eliminado
FULL_PATH = os.path.join(BASE_DIR, APPS_FOLDER)


def delete_migrations_files():

    num_compile_files = num_migrations_files = 0
    print ("\n Analizing your project .... \n")
    for (path, ficheros, archivos) in os.walk(FULL_PATH):
        # Si existe una carpeta entonces continua el flujo
        if 'migrations' in ficheros:
            for fichero in ficheros:  # <- Recorre los ficheros
                # Si encuentra una carpeta migrations entonces entra a ellas
                if fichero == "migrations":
                    migrations_path = os.path.join(path, fichero)
                    for (child_path, ficheros_2, archivos_2) in os.walk(migrations_path):  # NOQA
                        for archivo in archivos_2:
                            file_path = os.path.join(child_path, archivo)
                            # Si son compilados entonces eliminamos
                            if archivo[-3:] == "pyc":
                                os.remove(file_path)
                                print ("[Compiled File] "), file_path
                                num_compile_files = num_compile_files + 1
                            else:
                                # Excluye los archivos __init__.py
                                if not archivo == "__init__.py":
                                    # Si es un archivo *.py lo elimina
                                    if archivo[-2:] == "py":
                                        os.remove(file_path)
                                        print ("[Migration File] "), file_path
                                        num_migrations_files = \
                                            num_migrations_files + 1
    print ("\n ===================== Execution Summary =========================")
    if num_compile_files == 0 and num_migrations_files == 0:
        print ("All your migrations folder are empty. Nothing was deleted")
    else:
        print ("Python files", num_migrations_files)
        print ("Compiled Python files", num_compile_files)
    print ("=================================================================\n")


def user_yes_no_query():
    """
    Función muestra en pantalla un aviso para que el usuario responde YES o NO.
    Si responde YES --> Se ejecuta la función delete_migrations_files()
    Si responde NO ---> La función se detiene sin ninguna acción a ejecutar.
    Si responde algo más --> La función solicita escribir respuesta válida Y/N.
    """
    sys.stdout.write(
        'Are you sure you want to delete all migrations files? [y/n]: ')
    while True:
        try:
            respuesta = strtobool(input().lower())
            if respuesta:
                delete_migrations_files()
            else:
                sys.stdout.write('\nOk, nothing was deleted\n\n')
            return True
        except ValueError:
            sys.stdout.write('Please enter: \'y\' o \'n\'.\n')

user_yes_no_query()