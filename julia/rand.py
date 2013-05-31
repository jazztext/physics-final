#!/usr/bin/env python

# Just a disclaimer, this is just a fun aside project for me
# Also it's useful for finding good example values for c
# Libraries!
import pygame
import pygame.gfxdraw
import cmath
import sys
import random

# Set initial conditions
width=800
height=700
ppu=200

# Declare variables
x=0
y=0
r=random.uniform(-1,1)
i=random.uniform(-1,1)
c=complex(r,i)

# Define f(n)
def f(n):
	n=n*n
	return n

# Color processing, cyan to black
def colortest(i):
	if (i<=50):
		return (0,255-5*i,255-5*i)
	else:
		return (0,0,0)

# Actual processing
def julia(n,c):
	i=0
	while ((((n.real*n.real)+(n.imag*n.imag))**0.5)<2) and (i<51):
		n=f(n)+c
		i+=1
	return colortest(i)

# Main function
def main():
	# Assign random values to both real and imaginary parts of c
	print "-----------------------------------------------"
	r=random.uniform(-1,1)
	i=random.uniform(-1,1)
	c=complex(r,i)
	print "Using ",c," as c"
	
	# Initialize
	screen=pygame.display.set_mode((width,height))
	n=0+0j
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-width/2,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,julia(n/ppu,c))
		pygame.display.flip()

# Time for the part that actually runs!
while True:
	main()





