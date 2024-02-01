import cv2 as cv
import numpy as np

data_dir = 'PROGRAMACION_DE_IA/Espacios_de_Color/imagenes/'

def click_raton(event, x, y, flags, param):
    global color_punto
    if event == cv.EVENT_LBUTTONDBLCLK:
        b, g, r = img1[y, x]
        color_punto = np.uint8([[[b, g, r]]])
        color_punto = cv.cvtColor(color_punto, cv.COLOR_BGR2HSV)
        print(f'Click en {x}, {y}, color= {color_punto}')

src1 = cv.VideoCapture(0)
cv.namedWindow('Fondo')
global mascara
mascara=None
global fondo
fondo=None
# src2=cv.imread(data_dir+'fondo.png')
color_punto=None 

while True:
    ret, img1 = src1.read()

    hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
    if color_punto is not None:
        color_minimo = np.array([color_punto[0, 0, 0] - 10, 10, 10])
        color_maximo = np.array([color_punto[0, 0, 0] + 10, 255, 255])
        mascara = cv.inRange(hsv, color_minimo, color_maximo)
        cv.imshow('Mascara', mascara)
        color_punto = None
    cv.imshow("Objeto", img1)
    cv.setMouseCallback('Objeto', click_raton)
    
    if mascara is not None and fondo is not None:

        fondo_imagen = cv.bitwise_and(mascara, fondo)
        not_mascara = cv.bitwise_not(mascara)
        nomascara_fibdi = cv.bitwise_and(not_mascara,img1)
        img1 = cv.bitwise_or(fondo_imagen,nomascara_fibdi)
    

    if cv.waitKey(10) & 0xFF == 32:
       fondo=img1.copy()
       cv.imshow('Fondo',fondo)

    if cv.waitKey(10) & 0xFF == 27:
        break
    

    # fondo and mascara
    # not a la mascara
    # mascara and objeto
    # (fondo and mascara)or (mascara and objeto)




