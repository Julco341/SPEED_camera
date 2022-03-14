import cv2 as cv
import time
import numpy as np
# coding: utf-8

path = '/home/julien/Map/PTAT.png'

image = cv.imread(path) #Image used at the back
clone = image.copy()	#Image clone we are writing on

cv.namedWindow('map', cv.WINDOW_AUTOSIZE)

while(1):
	try:
		clone = image.copy() #Cloning the image
		fichier = open('output.txt','r') #Reading the Optitrack position file
		nmbrb= fichier.readline() #Reading the number of rigid body
		#print(nmbrb)
		for i in range(int(nmbrb)):
			coord = fichier.readline()#Reading the line
			coord_list=coord.split(' ',4)
			#print (coord)
			x=float(coord_list[1])
			z=float(coord_list[3])
			#print (x,z)
			x1=int((1.9-x)*250)	#Ratio
			z1=int((2.95+z)*250)	#Ratio
			#print (x1,z1)
			cv.putText(clone, coord_list[0],(z1,x1),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,2)
			#cv.circle(image,(z1,x1),5,(0,0,255),-1) #Tracer
			cv.circle(clone,(z1,x1),5,(0,0,255),-1)
		#cv.imshow('map',image) #Tracer
		cv.imshow('map', clone)
		cv.waitKey(300)
		fichier.close()
	except Exception:
		pass


cv.waitKey(0)

cv.destroyAllWindows()

