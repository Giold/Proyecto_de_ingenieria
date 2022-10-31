from encodings import utf_8
import sys
import os
import re
import time # libreria para cronometrar
from bs4 import BeautifulSoup # libreria para eliminar tags html - (pip install beautifulsoup4)
from prettytable import PrettyTable

archivos = r"C:\Users\USER\Documents\GitHub\Proyecto_de_ingenieria\Actividad5ArchivoDuplicado\Files" # Carpeta de archivos html
archivosfix = r"C:\Users\USER\Documents\GitHub\Proyecto_de_ingenieria\Actividad5ArchivoDuplicado\Codigo\FilesFix" # Carpeta para almacenar archivos html sin etiquetas
archivosList = r"C:\Users\USER\Documents\GitHub\Proyecto_de_ingenieria\Actividad5ArchivoDuplicado\Codigo\FilesList" # Carpeta para almacenar lista de texto de los html
archivosToken = r"C:\Users\USER\Documents\GitHub\Proyecto_de_ingenieria\Actividad5ArchivoDuplicado\Codigo\FilesToken" # Carpeta para almacenar listas tokenizadas

#Funcion para abrir y cronometrar los archivos 
def open_file():

    startF = time.perf_counter()
    total = 0
    
    sys.stdout = open("A1_matricula.txt", "w+")

    for filename in os.listdir(archivos):
        start = time.time()
        with open(os.path.join(archivos, filename), "r",  errors= "ignore") as f:
            end = time.time()
            total+= (end - start)

            print("Proyecto_IDS/files/"+filename, "\t", end - start)
            endF = time.perf_counter()

    print("\ntiempo total en abrir los archivos:", f"{total:.2f}", "segundos")
    print("\ntiempo total de ejecucion:", f"{endF-startF:.2f}", "segundos")

    sys.stdout.close()

#Funcion para remover las etiquetas de los archivos html
def remove_html_tags():

    startF = time.perf_counter()
    total = 0

    sys.stdout = open("A2_matricula.txt", "w+")

    for filename in os.listdir(archivos):
        start = time.time()
        with open(os.path.join(archivos, filename), "r",  errors= "ignore") as f:

            with open(os.path.join(archivosfix, filename), 'w') as outfile: 
                soup = BeautifulSoup(f,'html.parser').text # Remover tags de html
                outfile.write(str(soup)) # Escribir datos en el archivo
                end = time.time()
                total+= (end - start)

        print("Proyecto_IDS/files/"+filename, "\t", end - start)
        endF = time.perf_counter()

    print("\ntiempo total en abrir los archivos:", f"{total:.2f}", "segundos")
    print("\ntiempo total de ejecucion:", f"{endF-startF:.2f}", "segundos")

    sys.stdout.close()

#Funcion para crear lista de palabras en orden alfabetico
def create_list():
    
    startF = time.perf_counter()
    total = 0
    arc = list() 

    sys.stdout = open("A3_A4_matricula.txt", "w+") #creacion de txt con los tiempos

    for filename in os.listdir(archivos):
        start = time.time()
        with open(os.path.join(archivosfix, filename), "r",  ) as f:
                      
            with open(os.path.join(archivosList, filename), 'w+') as outfile:
                    for lines in f:
                        line = re.sub(r"(\d+)", '', lines) # Remover numeros
                        line = re.sub(r"[^\w\s]","", line) # Remover caracteres especiales (r"[^\w\s]","", line)
                        #line = re.sub(r"(\s)","", line) # Remover caracteres especiales (r"[^\w\s]","", line)
                        line = re.sub(r"\n","", line)# Remover saltos de linea 
                        line = re.sub(r"_","", line) # Remover guiones bajos
                        line = line.lower().split()# Divison de texto y poner en minusculas
                        arc.extend(line) # Unir palabras a una lista

                    arc.sort() # Ordenar lista de manera alfabetica
                    arc = "\n".join(arc) # Realizar salto de linea (Se convierte en String)
                    outfile.writelines(arc) # Escribir lista en el archivo
                    arc = list() # Convertir en Lista de nuevo
                    arc.clear() # Reinicar lista
                    
                    end = time.time()
                    total+= (end - start)
        
        print("Proyecto_IDS/files/"+filename, "\t", end - start)
        endF = time.perf_counter()

    print("\ntiempo total en crear los nuevos archivos:", f"{total:.2f}", "segundos")
    print("\ntiempo total de ejecucion:", f"{endF-startF:.2f}", "segundos")

    sys.stdout.close()

#Funcion para realizar el conteo de palabras y eliminas duplicadas
def tokenization():

    startF = time.perf_counter()
    total = 0
    count = dict()

    sys.stdout = open("A5_matricula.txt", "w+") #creacion de txt con los tiempos

    for filename in os.listdir(archivos):
        start = time.time()
        with open(os.path.join(archivosList, filename), "r") as f:
                      
            with open(os.path.join(archivosToken, filename), 'w+') as outfile:
                    for word in f:
                        word = re.sub(r"\n","", word) #Eliminar saltos de linea
                        if word in count: #Si la palabra esta en el conteo suma
                            count[word]+=1 
                        else:             #Si no, es la primera vez que aparece la palabra
                            count[word] = 1 

                    for key, value in count.items(): 
                        value = str(value) 
                        outfile.write(key+" "+value+"\n")
                    
                    count.clear()
                    end = time.time()
                    total+= (end - start)
        
        print("Proyecto_IDS/files/"+filename, "\t", end - start)
        endF = time.perf_counter()

    print("\ntiempo total en crear los nuevos archivos:", f"{total:.2f}", "segundos")
    print("\ntiempo total de ejecucion:", f"{endF-startF:.2f}", "segundos")

    sys.stdout.close()

#Funcion para realiza un conteo de las palabras en los archivos y crear una tabla en ascii con los mismos (SIN TERMINAR)
def Ascii():
    
    startF = time.perf_counter()
    total = 0
    countTotalAr = dict()
    countTotal = dict()

    mytable = PrettyTable(["Token","Repeticiones","# de archivos con ese token"]) #,"# de archivos con ese token"

    sys.stdout = open("A6_matricula.txt", "w+") #creacion de txt con los tiempos

    for filename in os.listdir(archivos):
        start = time.time()
        with open(os.path.join(archivosToken, filename), "r") as f:
                
            #with open(os.path.join(archivosList, filename), 'r') as outfile:
                    for word in f: # Saber la cantidad de archivos que contienen una misma palabra                      
                        word = re.sub(r"\n","", word)
                        number=(re.sub(r"\s","",word))#Quitar el espacio en blanco
                        number=int(re.sub(r"(\D+)","",word))#Quitar los no numeros
                        word = re.sub(r"(\d+)", '', word)#Quita los numeros                    
                        
                        if word in countTotalAr:
                            countTotalAr[word]+=number
                            countTotal[word]+=1
                        else:
                            countTotalAr[word] = number
                            countTotal[word]=1
                    
                    #for word in outfile:                       
                        #word = re.sub(r"\n","", word) #Eliminar saltos de linea

                        #if word in countTotal: #Si la palabra esta en el conteo suma
                            #countTotal[word]+=1 
                        #else:             #Si no, es la primera vez que aparece la palabra
                            #countTotal[word] = 1

                    end = time.time()
                    total+= (end - start)

        print("Proyecto_IDS/files/"+filename, "\t", end - start)
        endF = time.perf_counter()

    #countTotal.update(countTotalAr)
    with open("Token_List.txt","w") as fin:   
        for key, value in countTotalAr.items():             
            value = str(value)           
            value_2= str(countTotal.get(key))
            #fin.write(key+", "+value+", "+value_2+"\n")            
            mytable.add_row([key,value,value_2])        
        stingtable= mytable.get_string()
        fin.write(stingtable)
    #with open("Token_List.txt","w") as fin:
    #        for key, value in countTotalAr.items():
    #            value = str(value)
     #           value = "\n".join(value)
      #          fin.write(value)   

    print("\ntiempo total en acumular el diccionario:", f"{total:.2f}", "segundos")
    print("\ntiempo total de ejecucion:", f"{endF-startF:.2f}", "segundos")
     

    sys.stdout.close()  
    
    


#Ejecucion de funciones
open_file()
remove_html_tags()
create_list()
tokenization()
Ascii()

