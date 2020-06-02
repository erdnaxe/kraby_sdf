#!/usr/bin/env python3
import pybullet as p
import time
import pybullet_data
import os

p.connect(p.GUI)

p.setGravity(0, 0, -9.81)

# Load a ground
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadSDF("plane_stadium.sdf")

# Load robot, as SDFormat can contain multiple object, we select the first one
# r will contain the robot object id
p.setAdditionalSearchPath(os.getcwd())
r = p.loadSDF("hexapod.sdf")[0]

# Get all motorized joints id and name (which are revolute joints)
motorized_joints = [(j, p.getJointInfo(r, j)[1].decode())
                    for j in range(p.getNumJoints(r))
                    if p.getJointInfo(r, j)[2] == p.JOINT_REVOLUTE]

# Create user debug interface
motorized_joints_param = [(j, p.addUserDebugParameter(name, -0.5, 0.5, 0))
                          for j, name in motorized_joints]

while True:
    # Read user input and simulate motor
    for j, param in motorized_joints_param:
        angle = p.readUserDebugParameter(param)
        p.setJointMotorControl2(r, j, p.VELOCITY_CONTROL,
                                targetVelocity=angle)

    p.stepSimulation()

p.disconnect()

