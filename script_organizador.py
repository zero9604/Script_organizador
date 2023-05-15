import os
import shutil

def main():
    imagenes = ('bmp', 'gif', 'jpg', 'jpeg', 'jpe', 'jfif', 'tif','tiff', 'png')
    audio = ('wav', 'wave', 'aiff', 'pcm', 'flac', 'm4a','wma', 'wmv', 'mp3', 'ogg', 'aac')
    ejecutables = ('exe', 'py')
    pdf = ('pdf', 'PDF')
    office = ('doc', 'docx', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx')
    comprimidos = ('zip', 'rar', 'tar')

    # Creamos carpetas
    carpetas()

    # Listamos los archivos en el directorio actual
    archivos = os.listdir()

    for archivo in archivos:
        if os.path.isfile(archivo):
            extension = archivo.split('.')[-1]

            if extension in imagenes:
                mover(archivo, 'Downloaded Pictures')
            elif extension in audio:
                mover(archivo, 'Downloaded Music')
            elif extension in pdf:
                mover(archivo, 'Downloaded PDFs')
            elif extension in ejecutables and archivo.split('.')[0] != os.path.basename(__file__).split('.')[0]:
                # mueve cualquier archivo ejecutable que no sea el mismo
                mover(archivo, 'Downloaded Executables')
            elif extension in office:
                mover(archivo, 'Downloaded Office Files')
            elif extension in comprimidos:
                mover(archivo, 'Downloaded Compressed Files')

def carpetas():

    directorios = ('Downloaded Pictures','Downloaded Music','Downloaded PDFs','Downloaded Executables', 'Downloaded Office Files',
                   'Downloaded Compressed Files')
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