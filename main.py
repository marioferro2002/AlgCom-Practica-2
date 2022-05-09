import sys
from findpeaks import findpeaks
import random
import numpy as np

def image_generator(n_size=10):
    img= [[random.randint(0,255) for i in range(n_size)] for j in range(n_size)]
    fp = findpeaks(method='mask', whitelist='peak', scale=False, denoise=None, verbose=0)
    result = fp.fit(img)
    solution = np.argwhere(result['Xdetect'] == True)
    return {
        "image": img,
        "solution": solution.tolist()
    }

# TODO: Realizar cada una de vuestras funciones para detectar barcos dentro de la imagen de entrada que se encuentra en la variable "image2D".
def shipDetector(image):
    checked_Ships = []
    for line in range(len(image)):
        for column in range(len(image)):
            checked_Ships = check_near_ships(image, checked_Ships, line, column)
    print("Llista resultant" + str(checked_Ships))
    return checked_Ships

def check_near_ships(image, checked_ship, line, column):
    directions = directions_avaliable(image, line, column)
    for direction in directions:
        #print("Valors a comparar: " + str(image[line][column]) + " " + str(image[direction[0]][direction[1]]))
        if(image[line][column] < image[direction[0]][direction[1]]):
            return checked_ship

    checked_ship.append([line, column])
    return checked_ship
#TODO: En este programa, debereis generar las imagenes de costos correspondientes tal y como hicimos en laboratorios y en la práctica 1.

def directions_avaliable(image, line, column):
    directions = []
    directions.append([line - 1, column])
    directions.append([line + 1, column])
    directions.append([line, column - 1])
    directions.append([line, column + 1])

    for direction in directions:
        if -1 in direction or (len(image)) in direction:
            directions.remove(direction)
    #print(" Tamany maxim del array: " + str(len(image)) + ", posicio " + str(line) + " " + str(column) + ", direccions disponibles : " + str(directions))
    return directions

# Programa principal para la generación de las matrices 2D y la identificación de barcos.
if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <matrix_size_number>')

    image2D= image_generator (int(sys.argv[1]))

    print (image2D)


