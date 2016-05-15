# try it out at https://repl.it/CQvn

import math

def get_target(x_pos, y_pos, direction, max_x = 225.0, max_y = 180.0):
	x_rem = max_x - x_pos
	print "x_rem = ", x_rem
	rad = float(direction) / max_y * math.pi
	print "rad = ", rad
	tan = math.tan(rad)
	print "tan = ", tan
	y_rem = x_rem / tan
	print "y_rem = ", y_rem
	target = y_pos + y_rem
	print "target = ", target
	return target

def resolve_bounces(target, max_y = 180.0):
	while target > max_y or target < - max_y:
		if target > max_y:
			target = 2 * max_y - target
		if target < - max_y:
			target = -2 * max_y - target
		print "target -> ", target
	return target
	
def find_bounce(x_pos, y_pos, direction, max_y = 180.0):
	rad = direction / max_y * math.pi
	print "rad = ", rad
	tan = math.tan(rad)
	print "tan = ", tan
	if tan > 0:
		y_rem = max_y - y_pos
		y_bounce = max_y
	else:
		y_rem = y_pos + max_y
		y_bounce = -max_y
	print "y_rem = ", y_rem
	print "y_bounce = ", y_bounce
	x_rem = y_rem * tan
	print "x_rem = ", x_rem
	x_bounce = x_pos + x_rem
	print "x_bounce = ", x_bounce
	return x_bounce, y_bounce

def advance(x_pos, y_pos, direction, amount=10, max_y = 180.0):
	rad = direction / max_y * math.pi
	print "rad = ", rad
	x_pos += amount * math.sin(rad)
	y_pos += amount * math.cos(rad)
	return x_pos, y_pos

#resolve_bounces(get_target(-51, -124, 29)) -> -13.9
#resolve_bounces(get_target(121.6, 150.4, 151)) -> -36

