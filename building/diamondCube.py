import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

# enter into IDE
# pos
# Vec3(34,1,46)

# set diamond cube
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+10, pos.y + 10, pos.z +10, 57)

# put yourself on top of diamond cube
mc.player.setTilePos(pos.x+10, pos.y+10, pos.z+10)
