import numpy as np
from .objmesh import *

class Entity:
    def __init__(self):
        pass

    def render(self):
        """
        Draw the object
        """
        raise NotImplementedError

    def step(self, delta_time):
        """
        Update the state of the object
        """
        raise NotImplementedError

class Agent(Entity):
    def __init__(self):
        # Position of the agent (at floor level)
        self.position = np.array([0, 0, 0])

        # Direction angle in radians
        # Angle zero points towards the positive X axis
        self.direction = 0

        # Distance between the camera and the floor
        self.cam_height = 1.5

        # Camera up/down angle
        self.cam_angle = 0

        # Vertical field of view
        self.cam_fov_y = 45

    @property
    def dir_vec(self):
        """
        Vector pointing in the direction of forward movement
        """

        x = math.cos(self.direction)
        z = -math.sin(self.direction)
        return np.array([x, 0, z])

    @property
    def right_vec(self):
        """
        Vector pointing to the right of the agent
        """

        x = math.sin(self.direction)
        z = math.cos(self.direction)
        return np.array([x, 0, z])

    @property
    def cam_pos(self):
        return self.position + np.array([0, self.cam_height, 0])

    @property
    def cam_dir(self):
        # FIXME: take cam_angle into account
        return self.dir_vec

    def step(self, delta_time):
        pass