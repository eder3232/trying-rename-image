import os

# Ruta del directorio que contiene la imagen
directorio = "./images"

# Nombre de la imagen que deseas cambiar
nombre_original = "1.jpg"

# Construir la ruta completa del archivo original
ruta_original = os.path.join(directorio, nombre_original)

# Construir el nuevo nombre de la imagen con extensión en mayúsculas
nombre_nuevo = "1.JPG"

# Construir la ruta completa del archivo con el nuevo nombre
ruta_nueva = os.path.join(directorio, nombre_nuevo)

# Cambiar el nombre del archivo
os.rename(ruta_original, ruta_nueva)

print(f"Nombre cambiado de {nombre_original} a {nombre_nuevo}")
