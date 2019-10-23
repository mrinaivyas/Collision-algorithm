from vpython import *
import numpy as np
import fcl




floor = box (pos=vector(0,0,0), length=30, height=30, width=30, color=color.blue, opacity = 0.2)
ball1 = sphere (pos=vector(0,3,0), radius=1, color=color.red)
ball1.velocity = vector(0,-5,0)
ball2 = sphere (pos=vector(0,-3,0), radius=1 , color=color.blue)
ball2.velocity = vector(0,5,0)
dt = 0.01
T = np.array([1.0, 2.0, 3.0])
ball3 = sphere (pos=vector(0,-10,0), radius=1, color=color.red)
ball3.velocity = vector(0,5,0)
ball4 = sphere (pos=vector(0,10,0), radius=1, color=color.red)
ball4.velocity = vector(0,-3,0)

def collision_obj(p):
	
	geom = fcl.Sphere(1.0)
	T =[ball.pos.x,ball.pos.y,ball.pos.z]
	t = fcl.Transform(Tp) 
	obj = fcl.CollisionObject(geom, tp)

def collision(ball1 ,ball2, ball3, ball4):

	geom1 = fcl.Sphere(1.0)
	geom2 = fcl.Sphere(1.0)

	geom3 = fcl.Sphere(1.0)
	geom4 = fcl.Sphere(1.0)

	T1 =[ball1.pos.x,ball1.pos.y,ball1.pos.z]
	t1 = fcl.Transform(T1) 
	obj1 = fcl.CollisionObject(geom1, t1)

	T2 =[ball2.pos.x,ball2.pos.y,ball2.pos.z]
	t2 = fcl.Transform(T2) 
	obj2 = fcl.CollisionObject(geom2, t2)

	T3 =[ball3.pos.x,ball3.pos.y,ball3.pos.z]
	t3 = fcl.Transform(T3) 
	obj3 = fcl.CollisionObject(geom3, t3)

	T4 =[ball4.pos.x,ball4.pos.y,ball4.pos.z]
	t4 = fcl.Transform(T4) 
	obj4 = fcl.CollisionObject(geom4, t4)


	geoms = [geom1, geom2, geom3, geom4]
	objs = [obj1, obj2, obj3, obj4]
	names = ['obj1', 'obj2','obj3','obj4']

	# Create map from geometry IDs to objects
	geom_id_to_obj = { id(geom) : obj for geom, obj in zip(geoms, objs) }

	# Create map from geometry IDs to string names
	geom_id_to_name = { id(geom) : name for geom, name in zip(geoms, names) }

	# Create manager
	manager = fcl.DynamicAABBTreeCollisionManager()
	manager.registerObjects(objs)
	manager.setup()

	# Create collision request structure
	crequest = fcl.CollisionRequest(num_max_contacts=100, enable_contact=True)
	cdata = fcl.CollisionData(crequest, fcl.CollisionResult())

	# Run collision request
	manager.collide(cdata, fcl.defaultCollisionCallback)

	# Extract collision data from contacts and use that to infer set of
	# objects that are in collision
	objs_in_collision = set()

	for contact in cdata.result.contacts:
	    # Extract collision geometries that are in contact
	    coll_geom_0 = contact.o1
	    coll_geom_1 = contact.o2

	    # Get their names
	    coll_names = [geom_id_to_name[id(coll_geom_0)], geom_id_to_name[id(coll_geom_1)]]
	    coll_names = tuple(sorted(coll_names))

	    objs_in_collision.add(coll_names)

	for coll_pair in objs_in_collision:
		print('Object {} in collision with object {}!'.format(coll_pair[0], coll_pair[1]))
	return objs_in_collision

while 1:


	rate (100)
	
	ball1.pos = ball1.pos + ball1.velocity*dt
	if ball1.pos.y < (floor.pos.y -15.0):
		ball1.velocity.y = -ball1.velocity.y
	elif ball1.pos.y > (floor.pos.y + 15.0):
		ball1.velocity.y = -ball1.velocity.y

	ball2.pos = ball2.pos + ball2.velocity*dt
	if ball2.pos.y < (floor.pos.y -15.0):
		ball2.velocity.y = -ball2.velocity.y
	elif ball2.pos.y > (floor.pos.y + 15.0):
		ball2.velocity.y = -ball2.velocity.y
	
	ball3.pos = ball3.pos + ball3.velocity*dt
	if ball3.pos.y < (floor.pos.y -15.0):
		ball3.velocity.y = -ball3.velocity.y
	elif ball3.pos.y > (floor.pos.y + 15.0):
		ball3.velocity.y = -ball3.velocity.y
	
	ball4.pos = ball4.pos + ball4.velocity*dt
	if ball4.pos.y < (floor.pos.y -15.0):
		ball4.velocity.y = -ball4.velocity.y
	elif ball4.pos.y > (floor.pos.y + 15.0):
		ball4.velocity.y = -ball4.velocity.y

	collied_objs = collision(ball1,ball2,ball3,ball4)

	
