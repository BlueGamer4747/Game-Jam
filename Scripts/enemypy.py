import bge
import mathutils

def main():
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    enemy = cont.owner
    
    # Try to find the player in the scene
    player = scene.objects.get("Player")
    
    if player:
        # Get positions of both objects
        enemy_pos = enemy.worldPosition
        player_pos = player.worldPosition
        
        # Calculate distance vector and actual distance
        vector = player_pos - enemy_pos
        distance = vector.length
        
        # Set detection range threshold (e.g., 15 units)
        if distance < 15.0 and distance > 1.0:
            # Normalize vector to get direction and scale by speed
            vector.normalize()
            speed = 0.05
            enemy.applyMovement(vector * speed, True)
            
            # Look at the player
            enemy.alignAxisToVect(vector, 1, 0.2)

main()
