#!/usr/bin/env python


# Libraries!
import pygame
import pygame.gfxdraw
import cmath

# Far less options than the julia set generator!
width=1000
height=750
ppu=280

# Declarations of variables!
x=0
y=0
n=0+0j
	
# Function of n, should NOT be changed
def f(n):
	n=n*n
	return n

# Color processing! Smooth gradient from cyan to black!
def colortest(i):
	if (i<=10):
		return (0,255-5*i,255-5*i)
	elif (i<=50):
		return (0,255-5*i,255-5*i)
	else:
		return (0,0,0)


# Actual processing!
def mandel(n):
	i=0
	z=0+0j
	while ((((z.real*z.real)+(z.imag*z.imag))**0.5)<2) and (i<51):
		z=f(z)+n
		i+=1
	return colortest(i)
	
def keep():
	# Keep the window open until the close signal is given!
	running=True
	while running:
		pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False


# Main function 
def main():
	# Initialize screen
	screen=pygame.display.set_mode((width,height))
	# Calculate by rows, then columns
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-3*width/4,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,mandel(n/ppu))
		# Display line by line
		pygame.display.flip()
	keep()

# The actual running part of the program!
main()




