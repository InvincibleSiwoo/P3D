from math import sin, cos, radians

from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
from P3Dcamera import Camera

import pygame
import os

script_location = os.path.realpath(__file__)

def init(size: tuple[int, int]):
    pygame.init()
    pygame.display.set_mode(size, DOUBLEBUF|OPENGL)
    pygame.display.set_caption(script_location)
    gluPerspective(45, (size[0]/size[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def loop(key_func=None, draw=None, camera=None):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if key_func != None:
                    key_func(event.key)
                if isinstance(camera, Camera):
                    if event.key == pygame.K_w:
                        camera.position.z += 1
                    elif event.key == pygame.K_s:
                        camera.position.z -= 1
                    elif event.key == pygame.K_a:
                        camera.position.x -= 1
                    elif event.key == pygame.K_d:
                        camera.position.x += 1
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                if isinstance(camera, Camera):
                    max_angle = 85
                    min_angle = -85

                    pitch_change = sin(radians(x)) * 0.1
                    yaw_change = cos(radians(y)) * 0.1

                    camera.pitch = clamp(camera.pitch + pitch_change, min_angle, max_angle)
                    camera.roll = clamp(camera.roll + pitch_change, min_angle, max_angle)
                    camera.yaw = camera.yaw + yaw_change

                    camera.look()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if draw != None:
            draw()
        pygame.display.flip()


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
