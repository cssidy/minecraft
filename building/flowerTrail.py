# as seen in Learn To Program With Minecraft: Transform Your World With The Power of Python, written by Craig Richardson


from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y, pos.z, 38)
	time.sleep(0.2)
