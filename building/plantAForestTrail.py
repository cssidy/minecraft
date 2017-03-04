from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()

while True:
        pos = mc.player.getPos()
        choice = random.choice([39, 40, 6, 31, 32])
        state = random.choice([1, 2,])

        mc.setBlock(pos.x, pos.y, pos.z, choice, state)
                        
        time.sleep(0.2)

