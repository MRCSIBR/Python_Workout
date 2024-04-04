#!/usr/bin/python3

# Este script escribe texto a output de consola
import sys
import time

frase1 = 'Bienvenido a asistente artificial de Codigo.'

frase2 = 'This is a very long string that\n' \
        'doesn\'t fit on a single line,\n' \
        'so we split it into multiple lines.\n' \
        'To fill the screen'

frase3 = 'Welcome to the world of Artificial Intelligence! AI is transforming the world in many positive ways\n'


def escritor(frase):

    for letter in frase:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.02)

    print(' \n')

escritor(frase1)
escritor(frase2)
escritor(frase3)
