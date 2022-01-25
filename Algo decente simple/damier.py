from tkinter import *
from random import randrange


taille_carre = 80
fen = Tk()
can = Canvas(fen, width = taille_carre * 8, height = taille_carre * 8, bg = "white")

def damier():
	"Trace le damier"
	y = 0
	while y < 8:
		if y % 2 == 0: # Décale une fois sur deux 
			x = 0      # la position du premier carré noir
		else:
			x = 1
		carre_noir(x*taille_carre, y*taille_carre)
		y += 1



def carre_noir(x, y):
	"Trace les carrés noirs"
	i = 0
	while i < 4:
		can.create_rectangle(x, y, x+taille_carre, y+taille_carre, fill = "#2cb")
		i += 1
		x += taille_carre * 2


def pion(x,y):
	"Dessine un pion au hazard sur le damier"
	creation_pion((taille_carre/2+x * taille_carre), (taille_carre/2+y * taille_carre), taille_carre/3, "yellow")


def creation_pion(x, y, r, coul):
	"Trace un pion"
	can.create_oval(x-r, y-r, x+r, y+r, fill = coul)
