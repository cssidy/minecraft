from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:
	pos = mc.player.getPos()

	# trunk
	mc.setBlock(pos.x, pos.y, pos.z, 17, 1)
	mc.setBlock(pos.x, pos.y+1, pos.z, 17, 1)
	mc.setBlock(pos.x, pos.y+2, pos.z, 17, 1)

	# canopy
	mc.setBlock(pos.x, pos.y+3, pos.z, 18, 1)
	mc.setBlock(pos.x, pos.y+4, pos.z, 18, 1)
	mc.setBlock(pos.x, pos.y+5, pos.z, 18, 1)

	mc.setBlock(pos.x+1, pos.y+3, pos.z, 18, 1)
	mc.setBlock(pos.x+1, pos.y+4, pos.z, 18, 1)
	mc.setBlock(pos.x+2, pos.y+4, pos.z, 18, 1)
	mc.setBlock(pos.x+1, pos.y+5, pos.z, 18, 1)

	mc.setBlock(pos.x-1, pos.y+3, pos.z, 18, 1)
	mc.setBlock(pos.x-1, pos.y+4, pos.z, 18, 1)
	mc.setBlock(pos.x-2, pos.y+4, pos.z, 18, 1)
	mc.setBlock(pos.x-1, pos.y+5, pos.z, 18, 1)

	mc.setBlock(pos.x+1, pos.y+3, pos.z+1, 18, 1)
	mc.setBlock(pos.x+1, pos.y+4, pos.z+1, 18, 1)
	mc.setBlock(pos.x+2, pos.y+4, pos.z+1, 18, 1)
	mc.setBlock(pos.x+1, pos.y+5, pos.z+1, 18, 1)

	mc.setBlock(pos.x-1, pos.y+3, pos.z-1, 18, 1)
	mc.setBlock(pos.x-1, pos.y+4, pos.z-1, 18, 1)
	mc.setBlock(pos.x-2, pos.y+4, pos.z-1, 18, 1)
	mc.setBlock(pos.x-1, pos.y+5, pos.z-1, 18, 1)
	
	

	time.sleep(2)
