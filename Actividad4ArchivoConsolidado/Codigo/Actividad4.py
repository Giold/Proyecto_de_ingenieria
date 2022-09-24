from pathlib import Path
from time import time
import re 

#Funcion para quitar etiquetas de HTML 
def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)

time_debug = time()
#Invocar carpeta de htmls.
#Al momento de pasar el codigo cambiar este valor al de la carpeta
Ruta = 'C:/Users/USER/Documents/GitHub/Proyecto_de_ingenieria/Actividad4ArchivoConsolidado/Files'

#manda a llamar el String de la variable ruta y la convierte en una ruta donde se ubica la informacion de los HTML's
DC = Path(Ruta)
totalTempFiles = 0

#a - Anexa.
#w - Eliminar o sobreescribir
#Se inicializa el archivo TXT donde va a ser ingresada la informacion de los HTML, junto con el tiempo de ejecucion 
txt = open ('TiemposHTML.log','a+')
txt.truncate(0)

#Metodo para el bucle, esto nos ayudara para colocar los htmls en el fichero y poder contar el tiempo y desplegarlo
for bucle in DC.iterdir():
    #Imprime en pantalla la cantidad de HTML
    print(bucle)

    #TI - Tiempo inicial
    TI = time()
    raw_html = open(bucle, errors= "ignore").read()

    #Se incializa el archivo TXT donde estara la informacion de los HTML sin las etiquetas en un TXT
    file = open('SinEtiquetas.txt', 'a+')
    file.write(strip_tags(raw_html))

    tiempofinal = time()
    tiempo_debugin = round(tiempofinal - TI, 6)
    txt.write (str(bucle) + " ------> " + str(tiempo_debugin) + "\n")

    totalTempFiles += tiempo_debugin
#Función para ayudar a sumar el tiempo de ejecución cuando se abren los archivos + el tiempo total.
tiempo_ef = time()
tiempo_all = round(tiempo_ef - TI, 6)
txt.write ("\n" + "Tiempo Total en quitar las Etiquetas HTML: " + str(round(totalTempFiles, 4)) + "\n")
txt.write ("Tiempo Total de Ejecucion: " + str(tiempo_all) + "\n")
txt.close()

#Actividad 3
def sorting(filename):
  #Abre el archivo llamado SinEtiquetas.txt
  infile = open('SinEtiquetas.txt')

  #Crea una cadena de palabras
  palabras = []

  #Crea un ciclo en anidado en el que abre la cadena, se crean y abre el archivo Resultado
  for line in infile:
    temp = line.split()
    for i in temp:
      [palabras.append(i.lower())] #Con el .lower se degrada palabra por palabra a minúsculas
  infile.close()
  palabras.sort()

  #Abre el archivo para escribir "W", si no existe el archivo lo crea
  outfile = open("Resultado.txt", "w")

  #Se imprime las palabras y pasa por linea decada palabra escrita 
  for i in palabras:
        #Hace el ciclo hasta que se acaben las palabras y pasa por otra linea. 
        outfile.writelines(i)
        outfile.writelines("\n")
  #Imprime las palabras en orden y cierra el archivo. 
  outfile.close()
sorting("Resultado.txt")