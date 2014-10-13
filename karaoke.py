#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Roger Urrutia Bayo

# os --> para poder descargar cosas
import os
import smallsmilhandler
import sys
from xml.sax import make_parser


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    # Constructor
    def __init__(self, fichero):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

    # muestro por pantalla las etiquetas y los atributos
    def __str__(self):
        for linea in self.lista:
            # Elemento
            print linea[0],
            valor = linea[1]
            for atributo in valor:
                if valor[atributo] != "":
                    # Atributos
                    print '\t', atributo, '=', valor[atributo],
            print

    # descarga en local el contenido multimedia contenido en src
    def do_local(self):
        for linea in self.lista:
            valor = linea[1]
            for atributo in valor:
                if valor[atributo] != "":
                    if atributo == "src":
                        recurso = valor[atributo]
                        os.system("wget -nv " + recurso)
                        # elimino la url quedandome solo con
                        # el nombre de fichero separo por el caracter '/'
                        nombre = recurso.split('/')
                        # me quedo solo con el nombre del fichero
                        nombre = nombre[-1]
                        valor[atributo] = nombre

        print

if __name__ == "__main__":
    # tiene que pasar el nombre del fichero smil
    try:
        fichero = sys.argv[1]
    except IndexError:
        print 'Usage: python karaoke.py src_file.smil'
        sys.exit()
    smil = KaraokeLocal(fichero)
    smil.__str__()
    smil.do_local()
    smil.__str__()
