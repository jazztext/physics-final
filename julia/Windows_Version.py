#!/usr/bin/env python


##############################################################
##      THIS VERSION IS MUCH MORE POORLY DOCUMENTED         ##
##      SERIOUSLY JUST LOOK AT THE OTHER VERSION            ##
##############################################################

##############################################################
##      HOWEVER THE OTHER VERSION HAS MANY MORE FEATURES    ##
##      THAT AREN'T USABLE ON WINDOWS DUE TO THE LACK OF    ##
##      ANY SORT OF (USABLE) COMMAND LINE INTERFACE         ##
##############################################################



##############################################################
##      SERSIOUSLY READ THE STUFF ABOVE, THIS IS PROBABLY   ##
##      OVERKILL BUT YOU KNOW WHATEVER                      ##
##############################################################


# Libraries!
import pygame
import pygame.gfxdraw
import cmath
import sys
import random
import argparse


#Asks for user input, to decide the c value
r=float(raw_input("Real part of c:"))
i=float(raw_input("Imaginary part of c:"))
c=complex(r,i)
width=700
height=700
ppu=200

# Declaration of variables, values at this point are unimportant
x=0
y=0
n=0+0j

q=2


# The function that will be iterated through, usually it should just be n*n
def f(n):
	n=n*n
	return n

# Color processing, makes a fairly steady gradient
# Change the positioning of the "255-5*i" statements
# For different colored gradients, but I prefer teal to black
def colortest(i):
	if (i<=50):
		return (0,255-5*i,255-5*i)
	else:
		return (0,0,0)


# Actual calculations!
# Due to multiple conditions, a while statement is preferable to a for
# Also the escape conditions of a julia or mandelbrot set state when the
# distance from the origin is >2, it will become infinitely large
def julia(n):
	i=0
	while ((((n.real*n.real)+(n.imag*n.imag))**0.5)<2) and (i<51):
		n=f(n)+c
		i+=1
	return colortest(i)

def keep():
	# Keep the window open until the close signal is given
	running=True
	while running:
		pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False


def main():
	# Initialize display
	screen=pygame.display.set_mode((int(width),int(height)))
	# Main process, processes by rows then columns
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-width/2,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,julia(n/ppu))
            pygame.display.flip()
	keep()

# Parts of the program that actually run!
main()





