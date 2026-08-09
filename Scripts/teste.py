from bge import logic
from math import radians

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

    # Apply movement relative to the cube’s rotation
    owner.applyMovement(move_vec, local=True)

    # Rotation (Q/E for yaw)
    if events[bge.events.QKEY] == bge.logic.KX_INPUT_ACTIVE:
        owner.applyRotation([0, 0, radians(rot_speed)], local=True)
    if events[bge.events.EKEY] == bge.logic.KX_INPUT_ACTIVE:
        owner.applyRotation([0, 0, radians(-rot_speed)], local=True)

# Main
controller = bge.logic.getCurrentController()
owner = controller.owner
update_movement(owner)
