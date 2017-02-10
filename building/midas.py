from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

air = 0
water = 9

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

    if blockBelow != air and blockBelow != water:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
