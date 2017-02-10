from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math

homeX = 2
homeZ = 4
pos = mc.player.getTilePos()
x = pos.x
z = pos.z
distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)
far = distance <= 50
mc.postToChat("Your home is nearby: " + str(far))
