from pathlib import Path
from time import time
import re 


def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)
time_debug = time()

#Cambiar por la ruta en donde esta al instalar
Rute = 'C:/Users/USER/Desktop/Fase 1/Fase 1/Actividades/Archivo4Consolidado/Files'


DC = Path(Rute)
totaltempfiles = 0


txt = open ('Impresion.log','a+')
txt.truncate(0)

#Metodo para 
for bucle in DC.iterdir():
    
    print(bucle)
    tiempoInicial = time()
    raw_html = open(bucle, errors= "ignore").read()
    file = open('SinEtiquetas.txt', 'a+')
    file.write(strip_tags(raw_html))
    tiempofinal = time()
    tiempo_debugin = round(tiempofinal - tiempoInicial, 6)
    txt.write (str(bucle) + " ------> " + str(tiempo_debugin) + "\n")
    totaltempfiles += tiempo_debugin
tiempo_ef = time()
tiempo_all = round(tiempo_ef - tiempoInicial, 6)
txt.write ("\n" + "Tiempo Total en quitar las Etiquetas HTML: " + str(round(totaltempfiles, 4)) + "\n")
txt.write ("Tiempo Total de Ejecucion: " + str(tiempo_all) + "\n")
txt.close()

def sorting(filename):
    
  infile = open('SinEtiquetas.txt')
  palabras = []
  for line in infile:
    temp = line.split()
    for i in temp:
      palabras.append(i)
  infile.close()
  palabras.sort()
  
  outfile = open("Resultado.txt", "w")
  
  for i in palabras:   
    outfile.writelines(i)
    outfile.writelines("\n")
    
  outfile.close()
sorting("Resultado.txt")