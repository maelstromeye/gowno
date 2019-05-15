#! /usr/bin/python

import json

p = {}
with open('../dh.json','r') as file:
	p = json.loads(file.read())

with open('../urdf_p.yaml','w') as file:
	for key in p.keys():
		theta, d, a, alfa = p[key]
		theta, d, a, alfa = float(theta), float(d), float(alfa), float(theta)
		
		file.write(key + ":\n")
		file.write(" joint_xyz: %s 0 %s\n" % (a, d))
		file.write(" joint_rpy: %s 0 0\n" % (alfa))
		file.write(" link_x_size: %s\n" % (a))
		file.write(" link_xyz: %s 0 0\n" % (a/2))
		file.write(" link_rpy: 0 0 0\n") 
