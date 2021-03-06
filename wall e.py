from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def Draw_Lines():

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)
    glVertex(-0.35, 0.35)
    glVertex(0.35, 0.35)
    glVertex(0.35, -0.35)
    glVertex(-0.35, -0.35)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(-0.1, 0.35)
    glVertex(-0.1, 0.2)
    glVertex(0.1, 0.35)
    glVertex(0.1, 0.2)
    glVertex(-0.35, 0.2)
    glVertex(0.35, 0.2)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.35, 0.35)
    glVertex(0.35, 0.35)
    glVertex(0.35, -0.35)
    glVertex(-0.35, -0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(0.35, -0.25)
    glVertex(0.45, -0.25)
    glVertex(0.45, -0.35)
    glVertex(0.35, -0.45)
    glVertex(0.25, -0.45)
    glVertex(0.25, -0.35)
    glVertex(0.35, -0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(-0.35, -0.25)
    glVertex(-0.45, -0.25)
    glVertex(-0.45, -0.35)
    glVertex(-0.35, -0.45)
    glVertex(-0.25, -0.45)
    glVertex(-0.25, -0.35)
    glVertex(-0.35, -0.35)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,1)
    glVertex(-0.35, -0.25)
    glVertex(-0.45, -0.25)
    glVertex(-0.45, -0.35)
    glVertex(-0.35, -0.45)
    glVertex(-0.25, -0.45)
    glVertex(-0.25, -0.35)
    glVertex(-0.35, -0.35)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,1)
    glVertex(0.35, -0.25)
    glVertex(0.45, -0.25)
    glVertex(0.45, -0.35)
    glVertex(0.35, -0.45)
    glVertex(0.25, -0.45)
    glVertex(0.25, -0.35)
    glVertex(0.35, -0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(0.25,-0.45)
    glVertex(0.35, -0.45)
    glVertex(0.35, -0.5)
    glVertex(0.3, -0.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.25, -0.45)
    glVertex(0.35, -0.45)
    glVertex(0.35, -0.5)
    glVertex(0.3, -0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(-0.25, -0.45)
    glVertex(-0.35, -0.45)
    glVertex(-0.35, -0.5)
    glVertex(-0.3, -0.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.25, -0.45)
    glVertex(-0.35, -0.45)
    glVertex(-0.35, -0.5)
    glVertex(-0.3, -0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(0.35,-0.465)
    glVertex(0.45,-0.465)
    glVertex(0.45,-0.485)
    glVertex(0.35,-0.485)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.35, -0.465)
    glVertex(0.45, -0.465)
    glVertex(0.45, -0.485)
    glVertex(0.35, -0.485)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(-0.35, -0.465)
    glVertex(-0.45, -0.465)
    glVertex(-0.45, -0.485)
    glVertex(-0.35, -0.485)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.35, -0.465)
    glVertex(-0.45, -0.465)
    glVertex(-0.45, -0.485)
    glVertex(-0.35, -0.485)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(0.45,-0.3)
    glVertex(0.6,-0.3)
    glVertex(0.6,-0.65)
    glVertex(0.45,-0.65)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.86, 0.96, 1)
    glVertex(-0.45, -0.3)
    glVertex(-0.6, -0.3)
    glVertex(-0.6, -0.65)
    glVertex(-0.45, -0.65)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(0.45, -0.3)
    glVertex(0.45, -0.65)
    glVertex(0.6, -0.3)
    glVertex(0.6, -0.65)
    glVertex(0.45,-0.3)
    glVertex(0.6,-0.3)
    glVertex(0.45,-0.35)
    glVertex(0.6,-0.35)
    glVertex(0.45,-0.4)
    glVertex(0.6,-0.4)
    glVertex(0.45,-0.45)
    glVertex(0.6,-0.45)
    glVertex(0.45,-0.5)
    glVertex(0.6,-0.5)
    glVertex(0.45,-0.55)
    glVertex(0.6,-0.55)
    glVertex(0.45,-0.6)
    glVertex(0.6,-0.6)
    glVertex(0.45,-0.65)
    glVertex(0.6,-0.65)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex(-0.45, -0.3)
    glVertex(-0.45, -0.65)
    glVertex(-0.6, -0.3)
    glVertex(-0.6, -0.65)
    glVertex(-0.45, -0.3)
    glVertex(-0.6, -0.3)
    glVertex(-0.45, -0.35)
    glVertex(-0.6, -0.35)
    glVertex(-0.45, -0.4)
    glVertex(-0.6, -0.4)
    glVertex(-0.45, -0.45)
    glVertex(-0.6, -0.45)
    glVertex(-0.45, -0.5)
    glVertex(-0.6, -0.5)
    glVertex(-0.45, -0.55)
    glVertex(-0.6, -0.55)
    glVertex(-0.45, -0.6)
    glVertex(-0.6, -0.6)
    glVertex(-0.45, -0.65)
    glVertex(-0.6, -0.65)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,0)
    glVertex(0.35,0.35)
    glVertex(0.375,0.325)
    glVertex(0.375,0.275)
    glVertex(0.35,0.275)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)
    glVertex(-0.35, 0.35)
    glVertex(-0.375, 0.325)
    glVertex(-0.375, 0.275)
    glVertex(-0.35, 0.275)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.35, 0.35)
    glVertex(0.375, 0.325)
    glVertex(0.375, 0.275)
    glVertex(0.35, 0.275)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.35, 0.35)
    glVertex(-0.375, 0.325)
    glVertex(-0.375, 0.275)
    glVertex(-0.35, 0.275)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0.87, 1)
    glVertex(-0.075,0.325)
    glVertex(0,0.325)
    glVertex(0,0.275)
    glVertex(-0.075,0.275)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.075, 0.325)
    glVertex(0, 0.325)
    glVertex(0, 0.275)
    glVertex(-0.075, 0.275)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.87, 0.97, 1)
    glVertex(0.2,0.275)
    glVertex(0.425,0.275)
    glVertex(0.425,0.15)
    glVertex(0.2,0.15)
    glVertex(0.2,0.2)
    glVertex(0.375,0.2)
    glVertex(0.375,0.225)
    glVertex(0.2,0.225)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.2, 0.275)
    glVertex(0.425, 0.275)
    glVertex(0.425, 0.15)
    glVertex(0.2, 0.15)
    glVertex(0.2, 0.2)
    glVertex(0.375, 0.2)
    glVertex(0.375, 0.225)
    glVertex(0.2, 0.225)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.87, 0.97, 1)
    glVertex(-0.2, 0.275)
    glVertex(-0.425, 0.275)
    glVertex(-0.425, 0.15)
    glVertex(-0.2, 0.15)
    glVertex(-0.2, 0.2)
    glVertex(-0.375, 0.2)
    glVertex(-0.375, 0.225)
    glVertex(-0.2, 0.225)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.2, 0.275)
    glVertex(-0.425, 0.275)
    glVertex(-0.425, 0.15)
    glVertex(-0.2, 0.15)
    glVertex(-0.2, 0.2)
    glVertex(-0.375, 0.2)
    glVertex(-0.375, 0.225)
    glVertex(-0.2, 0.225)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.87, 0.97, 1)
    glVertex(0.375,0.25)
    glVertex(0.425,0.25)
    glVertex(0.425,0.175)
    glVertex(0.375,0.175)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.375, 0.25)
    glVertex(0.425, 0.25)
    glVertex(0.425, 0.175)
    glVertex(0.375, 0.175)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.87, 0.97, 1)
    glVertex(-0.375, 0.25)
    glVertex(-0.425, 0.25)
    glVertex(-0.425, 0.175)
    glVertex(-0.375, 0.175)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.375, 0.25)
    glVertex(-0.425, 0.25)
    glVertex(-0.425, 0.175)
    glVertex(-0.375, 0.175)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,0)
    glVertex(-0.075,0.475)
    glVertex(0.075,0.475)
    glVertex(0.075,0.35)
    glVertex(-0.075, 0.35)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.075, 0.475)
    glVertex(0.075, 0.475)
    glVertex(0.075, 0.35)
    glVertex(-0.075, 0.35)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(-0.075, 0.4375)
    glVertex(0.075, 0.4375)
    glVertex(-0.075, 0.3875)
    glVertex(0.075, 0.3875)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,0)
    glVertex(-0.025, 0.55)
    glVertex(0.025, 0.55)
    glVertex(0.025, 0.475)
    glVertex(-0.025, 0.475)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.025, 0.55)
    glVertex(0.025, 0.55)
    glVertex(0.025, 0.475)
    glVertex(-0.025, 0.475)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.77, 0.96, 1)
    glVertex(0.25, 0.225)
    glVertex(0.375, 0.225)
    glVertex(0.375, 0.2)
    glVertex(0.25, 0.2)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(0.25, 0.225)
    glVertex(0.375, 0.225)
    glVertex(0.375, 0.2)
    glVertex(0.25, 0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.77, 0.96, 1)
    glVertex(-0.25, 0.225)
    glVertex(-0.375, 0.225)
    glVertex(-0.375, 0.2)
    glVertex(-0.25, 0.2)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 1)
    glVertex(-0.25, 0.225)
    glVertex(-0.375, 0.225)
    glVertex(-0.375, 0.2)
    glVertex(-0.25, 0.2)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex(0.3, 0.275)
    glVertex(0.3, 0.225)
    glVertex(0.3, 0.2)
    glVertex(0.3, 0.15)
    glVertex(-0.3, 0.275)
    glVertex(-0.3, 0.225)
    glVertex(-0.3, 0.2)
    glVertex(-0.3, 0.15)
    glEnd()

    #glBegin(GL_POLYGON)  #error shadow
    #glColor3f(1, 0.75, 0.2)
    #glVertex(-0.2, 0.25)
    #glVertex(-0.175, 0.25)
    #glVertex(-0.175, 0.2)
    #glVertex(-0.25, 0.2)
    #glVertex(-0.25, 0.225)
    #glVertex(-0.225, 0.225)
    #glVertex(-0.2, 0.225)
    #glEnd()

    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    a = 0.25
    b = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x= a * cos(theta)
        y= b * sin(theta)
        glVertex(x,y+0.65)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_POINTS)
    a = 0.25
    b = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = a * cos(theta)
        y = b * sin(theta)
        glVertex(x, y + 0.65)
    glEnd()

    glColor3f(0,0.57,1)
    glBegin(GL_POLYGON)
    r = 0.025
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.05 , y + 0.3 )
    glEnd()

    glColor3f(1, 0.42, 0.29)
    glBegin(GL_POLYGON)
    r = 0.0125
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.05, y + 0.3)
    glEnd()

    glColor3f(0.51, 0.78, 1)
    glBegin(GL_POLYGON)
    r = 0.035
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.15, y + 0.65)
    glEnd()

    glColor3f(0, 0.57, 1)
    glBegin(GL_POINTS)
    r = 0.035
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.15, y + 0.65)
    glEnd()

    glColor3f(0.51, 0.78, 1)
    glBegin(GL_POLYGON)
    r = 0.035
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.15, y + 0.65)
    glEnd()

    glColor3f(0, 0.57, 1)
    glBegin(GL_POINTS)
    r = 0.035
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.15, y + 0.65)
    glEnd()

    glColor3f(0.51, 0.78, 1)
    glBegin(GL_POLYGON)
    r = 0.0175
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.15, y + 0.65)
    glEnd()

    glColor3f(0.18, 0.63, 1)
    glBegin(GL_POINTS)
    r = 0.0175
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.15, y + 0.65)
    glEnd()

    glColor3f(0.51, 0.78, 1)
    glBegin(GL_POLYGON)
    r = 0.0175
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.15, y + 0.65)
    glEnd()

    glColor3f(0.18, 0.63, 1)
    glBegin(GL_POINTS)
    r = 0.0175
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.15, y + 0.65)
    glEnd()

    glColor3f(0.9, 0.95, 1)
    glBegin(GL_POLYGON)
    r = 0.009
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.145, y + 0.645)
    glEnd()

    glColor3f(0.9, 0.95, 1)
    glBegin(GL_POLYGON)
    r = 0.009
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.155, y + 0.645)
    glEnd()

    glColor3f(0.9, 0.95, 1)
    glBegin(GL_POLYGON)
    r = 0.011
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.16 + 0.003, y + 0.665)
    glEnd()

    glColor3f(0.9, 0.95, 1)
    glBegin(GL_POLYGON)
    r = 0.011
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.14 + 0.003, y + 0.665)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    r = 0.01
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.3, y - 0.475)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    r = 0.01
    for theta in np.arange(0, 2 * pi, 0.05):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.3, y - 0.475)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,0)
    glVertex(0.35,-0.25)
    glVertex(0.35,-0.35)
    glVertex(0.25,-0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)
    glVertex(-0.35, -0.25)
    glVertex(-0.35, -0.35)
    glVertex(-0.25, -0.35)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(0.35,-0.35)
    glVertex(0.25, -0.35)
    glVertex(-0.35, -0.35)
    glVertex(-0.25, -0.35)
    glEnd()

def display():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    Draw_Lines()

    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"wall-e")
glutDisplayFunc(display)
glutMainLoop()
