import bge
from collections import OrderedDict
from math import radians

#class Component(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
#    args = OrderedDict([
#    ])

class Component(bge.types.KX_PythonComponent):
    # Required: Define exposed properties/arguments in Blender UI
    args = {
         "speed": 0.1,
    }

    # REQUIRED: Called once when the object/game starts
    def start(self, args):
        # Initialize variables here
        self.owner = self.object  # UPBGE 0.3+ uses self.object
        pass

    # OPTIONAL / COMMON: Called every frame
    def update(self):
        # Frame update logic here
        pass

def update_movement(owner, speed=0.1, rot_speed=1.0):
    keyboard = bge.logic.keyboard
    events = keyboard.events

    # Movement (WASD)
    move_vec = [0.0, 0.0, 0.0]
    if events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE:
        move_vec[1] += speed  # Forward (Y-axis)
    if events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE:
        move_vec[1] -= speed  # Backward
    if events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE:
        move_vec[0] -= speed  # Left (X-axis)
    if events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE:
        move_vec[0] += speed  # Right

def update(controller):
    # Main
    keyboard = bge.logic.getCurrentController()
    owner = controller.owner
    update_movement(owner)