from mcpi.minecraft import Minecraft
mc = Minecraft.create()
answer = input("Create a lake here? Y/N ")

if answer == "Y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 20, pos.y + 20, pos.z + 20, pos.x - 20, pos.y - 20, pos.z - 20, 8)
    mc.postToChat("Boom!")