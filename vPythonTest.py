# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:23:41 2019

@author: amris
"""
from vpython import *

floor = box (pos=vector(0,4,0), length=8, height=8, width=4, color=color.blue, opacity = 0.2)
ball = sphere (pos=vector(0,6,0), radius=1, color=color.red)
ball.velocity = vector(0,-1,0)
dt = 0.01

while 1:
    rate (100)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
