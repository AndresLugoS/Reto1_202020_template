"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
import unicodedata as uni

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file,cmpfunction):
    sep=";"
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    
    return lst



def loadMoviesDetails ():
    lst = loadCSVFile("Data/themoviesdb/MoviesDetailsCleaned-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadMoviesCasting ():
    lst = loadCSVFile("Data/themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


# Req 3

def ConocerTrabajoDirector (lista1, lista2, nom):
    listaPelis=[]
    numpeliculas=0
    proPeliculas=0.0

    for x in range(1, lt.size(lista1)):
        y=lt.getElement(lista2, x)
        if (y["director_name"] == nom): 
            listaPelis.append(lt.getElement(lista1, x)["original_title"])
            numpeliculas += 1 
            proPeliculas = float(lt.getElement(lista1, x)['vote_average'])

    if numpeliculas != 0:

        promfinal= proPeliculas/numpeliculas
        print("La lista de peliculas es: ", listaPelis)
        print("El numero de peliculas dirigidas por el director es: ", numpeliculas)
        print("El promedio de la calificacion de las peliculas es: ", promfinal)

    else:

        print("Ha ocurrido un error, porfavor escriba el nombre de otro director")


#Req 4
def ConocerTrabajoActor (lista1, lista2, nom):
    listaPelis=[]
    numpeliculas=0
    proPeliculas=0.0
    posiblesDirectores={}
    
    for x in range(1,  lt.size(lista1)):
        if lt.getElement(lista2, x)["actor1_name"] == nom or lt.getElement(lista2, x)["actor2_name"] == nom or lt.getElement(lista2, x)["actor3_name"] == nom or lt.getElement(lista2, x)["actor4_name"] == nom or lt.getElement(lista2, x)["actor5_name"] == nom:
           listaPelis.append(lt.getElement(lista1, x)["original_title"])
           numpeliculas += 1
           proPeliculas += float(lt.getElement(lista1, x)['vote_average'])

           nom_direc=lt.getElement(lista2, x)["director_name"]
           if nom_direc in posiblesDirectores:
               posiblesDirectores[nom_direc] += 1
           else:
               posiblesDirectores[nom_direc] = 1

    
    
    if numpeliculas != 0:
        director=""
        i=0
        for x in posiblesDirectores:
            if posiblesDirectores[x] > i:
                i=posiblesDirectores[x]
                director = x

        promfinal= proPeliculas/numpeliculas
        print("La lista de peliculas es: ", listaPelis)
        print("El numero de peliculas en las que el actor ha partisipado son: ", numpeliculas)
        print("El promedio de la calificacion de las peliculas es: ", promfinal)
        print("El nombre del director con el que actor ha trabajado mas veces es: ", director)
    else:
        print("Ha ocurrido un error, porfavor escriba el nombre de otro actor")
    

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMoviesDetails()
                lstmovcas = loadMoviesCasting()
                

            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                director=input("Escriba el nombre de un director para saber toda la informacion: ")
                ConocerTrabajoDirector(lstmovies, lstmovcas, director)
                pass

            elif int(inputs[0])==4: #opcion 4
                Actor=input("Escriba el nombre de un actor para saber toda la informacion: ")
                ConocerTrabajoActor(lstmovies, lstmovcas, Actor)
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()


