import pybullet as p
import time
import pybullet_data
import os

p.connect(p.GUI)

p.setGravity(0, 0, -9.81)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadSDF("plane_stadium.sdf")

p.setAdditionalSearchPath(os.getcwd())
p.loadSDF("hexapod.sdf")

while True:
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()

