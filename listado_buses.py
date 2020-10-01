##Autor: Jorge Manuel Lozano Gómez

import requests
import os
import sys
from bs4 import BeautifulSoup

def parada(r,soup,url):
    #Comprueba que la peticion que devuelve es Code=200
    status_code = r.status_code
    if status_code == 200: 
        #Extraigo el numero de la parada y el nombre
        parada =soup.find('span',{'id':'lblParada'}).get_text()
        nombre_parada =soup.find('span',{'id':'lblNombre'}).get_text()
        #Devuelvo string con formato
        return("Parada n"+ parada + " : "+nombre_parada+" : "+url)
    else:
        # Si ya no existe la página y me da un 400
        return ("Error "+status_code)
        sys.exit()


def main():
    final = False

    #Abro un archivo donde guardare las paradas
    file = open("ParadasOurense.txt", "w")
    for i in range(1,652):

        #Construyo la Url
        url="http://consultasqrou.avanzagrupo.com:8088/default.aspx?parada="+str(i)

        #Realizo la peticion a la web
        r = requests.get(url)

        #Paso el contenido HTML de la web a un objeto BeautifulSoup()
        soup = BeautifulSoup(r.text, 'lxml')

        #Escribo en el archivo
        file.write (parada(r,soup,url)+os.linesep)
        print(i)# Para llevar conteo

    #Cierra el archivo
    file.close()
    

if __name__ == "__main__":
    main()



