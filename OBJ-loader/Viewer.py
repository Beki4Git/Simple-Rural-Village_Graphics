
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

from loader import *
pygame.init()
window = (800,800)
hx = window[0]/2
hy = window[1]/2
srf = pygame.display.set_mode(window, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)         

obj = OBJ('Model/Simple-rural-village.obj', swapyz=True)

obj.generate()

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = window
gluPerspective(90.0, width/float(height), 0.01, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)
glClearColor(1.0, 1.0, 1.0, 0.0)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 2
rotate = move = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 4: zpos = max(0.1, zpos-0.1)
            elif event.button == 5: zpos += 0.1
            elif event.button == 1: rotate = True
            elif event.button == 3: move = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1: rotate = False
            elif event.button == 3: move = False
        elif event.type == MOUSEMOTION:
            i, j = event.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslate(tx/20., ty/20., - zpos)
    glRotate(-90, 0, 0, 1)
    
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    obj.render()

    pygame.display.flip()