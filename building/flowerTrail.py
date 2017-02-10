from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y, pos.z, 38)
	time.sleep(0.2)
