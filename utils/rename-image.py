import os

carpeta = './imagesBorrar'

if os.path.exists(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        nuevo_nombre = "Yelitza" + nombre_archivo

        ruta_original = os.path.join(carpeta, nombre_archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        os.rename(ruta_original, ruta_nueva)

    print("¡Nombres cambiados exitosamente!")
else:
    print(f"La carpeta {carpeta} no existe.")