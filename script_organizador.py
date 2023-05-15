import os
import shutil
import pprint
def main():
    imagenes = ('bmp', 'gif', 'jpg', 'jpeg', 'jpe', 'jfif', 'tif','tiff', 'png')
    # Creamos carpetas
    carpetas()

    # Listamos los archivos en el directorio actual
    archivos = os.listdir()
    pprint.pprint(archivos)
    print('imag.en gif.gif'.split('.'))




def carpetas():

    directorios = ('Downloaded Pictures','Downloaded Music','Downloaded PDFs','Downloaded Executables')
    archivos = os.listdir()

    for i in directorios:
        if i not in archivos:

            # Crea la carpeta con el nombre que tenga la variable i en ese momento.
            os.mkdir(i) 
            print(f'Carpeta {i} creada.')
        else:
            print(f'La carpeta {i} ya existia.')

def mover(archivo, dest):

    # mueve un archivo desde la carpeta actual a la carpeta "dest"
    shutil.move(archivo, dest + '/' +  archivo)



if __name__ == '__main__':
    main()