from vedo import Sphere, Cube, show, load

# Create different 3D objects
hip_left = load('./data/multi_vis/hip_left.stl').color('#ffc800')
hip_right = load('./data/multi_vis/hip_right.stl').color('#aabcff')
vert_l1 = load('./data/multi_vis/vert_l1.stl').color('#453fcc')
vert_l2 = load('./data/multi_vis/vert_l2.stl').color('#f9999a')
vert_l3 = load('./data/multi_vis/vert_l3.stl').color('#54faac')
vert_l4 = load('./data/multi_vis/vert_l4.stl').color('#abcdef')
vert_l5 = load('./data/multi_vis/vert_l5.stl').color('#99ffa0')

# Show the objects together in the same window
show(hip_left, hip_right, vert_l1, vert_l2, vert_l3, vert_l4, vert_l5)
