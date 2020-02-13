# Karby the Hexapod -- Robot description files

SDF description of Kraby the hexapod.
It can be used to simulate the robot in Gazebo or BulletPhysics.

## Dependencies

### Debian/Ubuntu

Install Gazebo 10 from the official instructions.

### ArchLinux

Install `bullet` then compile `gazebo` from AUR.

## Running simulations

### with Gazebo

```bash
gazebo hexapod.sdf -u --verbose
```

### with PyBullet

See `simulation_demo.py`.
