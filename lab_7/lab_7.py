# -*- coding: utf-8 -*-
# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
# Из модуля random импортируем одноименную функцию random
from random import random
import numpy as np
import matplotlib.pyplot as plt
# объявляем массив pointcolor глобальным (будет доступен во всей программе)
global pointcolor

width, height = 800,600



def compile_shader(type, sourse) :
    id = glCreateShader(type)
    glShaderSource(id, sourse)
    glCompileShader(id)

    result = glGetShaderiv(id, GL_COMPILE_STATUS)
    if result == GL_FALSE :
        length = glGetShaderiv(id, GL_INFO_LOG_LENGTH)
        info = glGetShaderInfoLog(id)
        print('error ! : ', info)
        glDeleteShader(id)
        return None
    return id

def create__shader(vertexShader, fragmentShader) :
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vertexShader)
    fs = compile_shader(GL_FRAGMENT_SHADER, fragmentShader)

    glAttachShader(program, vs)
    glAttachShader(program, fs)

    glLinkProgram(program)
    glValidateProgram(program)
    glDeleteShader(vs)
    glDeleteShader(fs)

    return program

def draw():
    glClear(GL_COLOR_BUFFER_BIT)                    # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)            # Включаем использование массива вершин
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, pointcolor)

    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    glDrawArrays(GL_QUAD_STRIP, 0, len(pointdata))

    glDisableClientState(GL_VERTEX_ARRAY)           # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)            # Отключаем использование массива цветов

    vertexShader = """

    void main(){
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;

    }
    """
    fragmentShader = """
    uniform float Time;
    void main() {
    	gl_FragColor = vec4( abs(sin(Time)), 0.0, 0.0, 1.0);
    }"""

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)

    time = (glutGet(GLUT_ELAPSED_TIME)/1000.)
    K = 10.0
    Velocity = 1.0
    Amp = 0.13

    # location = glGetUniformLocation(shader, 'Time')
    # glUniform1f(location, time)
    uniforms = {
        'time': glGetUniformLocation(shader, 'Time'),
        'K': glGetUniformLocation(shader, 'K'),
        'Velocity': glGetUniformLocation(shader, 'Velocity'),
        'Amp': glGetUniformLocation(shader, 'Amp'),
        }
    glUniform1f(uniforms['time'], time)
    glUniform1f(uniforms['K'], K)
    glUniform1f(uniforms['Velocity'], Velocity)
    glUniform1f(uniforms['Amp'], Amp)


    glutSwapBuffers()                               # Выводим все нарисованное в памяти на экран

def Init_GL_Window(num_window, width, height) :
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutInit(sys.argv)
    glutCreateWindow(b"Shaders!")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glClearColor(0.2, 0.2, 0.2, 1)

    glRotatef(-20, 1, 0, 0)     # Поворот шейдера в нужную проекцию
    glRotatef(5, 0, 1, 0)

    glutMainLoop()


def main() :
    Init_GL_Window(0, width, height)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
