from vpython import *
import numpy as np
import fcl

class objInBox():
	def __init__(self, x,y,z, n, type):
			self.n = n
			self.type = type
			self.Pos, self.Vel ,self.Radius= genObjects(n, type)

	def genObjects(self, n, type, x,y,z):
		if type == 0: #sphere
			tempPos = np.random.rand(n,3)
			tempPos = tempPos * np.array([x,y,z])

			tempVel = np.random.rand(n,3)
			tempVel = tempVel * np.array([5,5,5])

			tempRad = np.random.rand(n,1)
			tempRad = tempRad * np.array([3])
		return tempPos, tempVel, tempRad


	def updatePos(self):
		dt = 0.01
		self.Pos = self.Pos - dt *self.Vel 
		# if ball1.pos.y < (floor.pos.y -15.0):
		# 	ball1.velocity.y = -ball1.velocity.y
		# elif ball1.pos.y > (floor.pos.y + 15.0):
		# 	ball1.velocity.y = -ball1.velocity.y

	def checkCollision(self):
		g1 = fcl.Sphere(self.Radius)
		t1 = fcl.Transform()
		o1 = fcl.CollisionObject(g1, t1)

		g2 = fcl.sphere(self.Radius)
		t2 = fcl.Transform()
		o2 = fcl.CollisionObject(g2, t2)
		
		request = fcl.CollisionRequest()
		result = fcl.CollisionResult()
		ret = fcl.collide(o1, o2, request, result)
		return result, ret  #result.is_collide is the required function

	def updateVel(self,)
		pass


class DrawObj(objInBox):
	def __init__(Sphere,Box):
		self.sphere = Sphere
		self.box = Box
		pass

	def objtype():
		if objInBox.type == 0:
			ball = sphere (pos=objInBox.Pos, radius=objInBox.Radius, color=color.red)
		if objInBox.type == 1:
			square = box (pos=objInBox.Pos, length=30, height=30, width=30, color=color.blue, opacity = 0.2)
			


