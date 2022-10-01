from pprint import pprint
from random import randint
from time import sleep

lab_width= 13
lab_height= 10
lab_entry= [lab_height//2+1,0]
lab_exit= [lab_height//2-1, lab_width-1]

def viewLab(lab): 
    pretty_lab= []
    for elemento in lab:
        pretty_lab.append ("".join(elemento))
    pretty_lab= "\n".join(pretty_lab)    
    print(pretty_lab)

def buildWalls(width,height):
    lab=[]
    for i in range(height):
        line=[]
        for j in range(width):
            if  i == 0 or i == height - 1:
                line.append(u"\u2588") 
            else:
                if j == 0 or j == width - 1:
                    line.append(u"\u2588") 
                else:
                    line.append(" ")         
        lab.append(line) 

    return(lab)


def buildEntryExit(lab,entrada, salida):
    lab[entrada[0]][entrada[1]]= "X"
    lab[salida[0]][salida[1]]= "!"
    return lab 

def findPosition(lab):
    for i,line in enumerate(lab):
        for j,column in enumerate(line):
            if "X" == column:
                return [i,j]


def moveRandomly(lab):
    #1 = arriba, 2= izquierda, 3= derecha, 4= abajo 
    direction = randint(1,4)
    old_X= findPosition(lab)
    if direction == 1:
        new_X= [old_X [0]-1,old_X[1]]

    if direction == 2:
        new_X= [old_X [0],old_X[1]-1]
    
    if direction == 3:
        new_X= [old_X [0],old_X[1]+1]

    if direction == 4:
        new_X= [old_X [0]+1,old_X[1]]

    if lab[new_X[0]][new_X[1]] == " ":
        lab = move(lab,old_X,new_X)

    return lab
    
def move(lab,old_X,new_X):
    lab[old_X[0]][old_X[1]]= "."
    lab[new_X[0]][new_X[1]]= "X"
    return lab

def buildInitialPath(lab,entry,exit):
    if entry[0] == exit [0]:
        for i in range(1,exit[1]):
            lab[entry[0]+1][entry[1]+i] = u"\u2588"
            lab[entry[0]-1][entry[1]+i] = u"\u2588"

    if entry[0] < exit [0]: #entrada arriba,salida abajo
        lab[entry[0]-1][entry[1]+1] = u"\u2588"
        lab[entry[0]][entry[1]+2] = u"\u2588" 
        for i in range(1,exit[0]-entry[0]):
            lab[entry[0]+i][entry[1]+2] = u"\u2588"  
        lab[exit[0]+1][entry[1]+1] = u"\u2588"
        lab[exit[0]+1][entry[1]+2] = u"\u2588"
        for i in range(entry[1]+3,exit[1]):
            lab[exit[0]+1][entry[1]+i] = u"\u2588"
            lab[exit[0]-1][entry[1]+i] = u"\u2588"

    if entry[0] > exit [0]: #entrada abajo,salida arriba
        lab[entry[0]+1][entry[1]+1] = u"\u2588"
        lab[entry[0]][entry[1]+2] = u"\u2588" 
        for i in range(1,entry[0]-exit[0]):
            lab[entry[0]-i][entry[1]+2] = u"\u2588"  
        lab[exit[0]-1][entry[1]+1] = u"\u2588"
        lab[exit[0]-1][entry[1]+2] = u"\u2588"
        for i in range(entry[1]+3,exit[1]):
            lab[exit[0]+1][entry[1]+i] = u"\u2588"
            lab[exit[0]-1][entry[1]+i] = u"\u2588"

    return lab 

def divisionMethod(lab,entrada,salida,
    inicio_linea_cuarto,inicio_columna_cuarto,final_linea_cuarto,final_columna_cuarto):

    linea_de_partida= randint(inicio_linea_cuarto+2,final_linea_cuarto-2)
    while linea_de_partida == entrada[0] or linea_de_partida == salida[0]:
        linea_de_partida= randint(inicio_linea_cuarto+2,final_linea_cuarto-2)
    columna_de_partida= randint(inicio_columna_cuarto+2,final_columna_cuarto-2)

    puerta_linea1=randint(inicio_columna_cuarto+1,columna_de_partida-1)
    puerta_linea2=randint(columna_de_partida+1,final_columna_cuarto-1)
    puerta_columna1=randint(inicio_linea_cuarto+1,linea_de_partida-1)
    puerta_columna2=randint(linea_de_partida+1,final_linea_cuarto-2)

    width= final_columna_cuarto-inicio_columna_cuarto
    height= final_linea_cuarto-inicio_linea_cuarto
    for i in range(width):
        for j in range(height):
            if i == columna_de_partida or j == linea_de_partida:
                if i != 0 and i != width-1 and j != 0 and j != height-1:
                    if i != puerta_linea1 and i != puerta_linea2 and j != puerta_columna1 and j != puerta_columna2:
                        lab[j][i] = u"\u2588"
            
    return lab 





    
#si se va a mover a unar posicion donde sabes que se va a quedar trabado

#codigo ejecutable 
miLab = buildWalls(lab_width,lab_height)

miLab = buildEntryExit(miLab,lab_entry,lab_exit)
# while findPosition(miLab) != lab_exit:
#    sleep(1)
#    miLab= moveRandomly(miLab)
#     viewLab(miLab)

#miLab = buildInitialPath(miLab,lab_entry,lab_exit)
miLab=divisionMethod(miLab,lab_entry,lab_exit,0,0,lab_height-1,lab_width-1)
viewLab(miLab)



