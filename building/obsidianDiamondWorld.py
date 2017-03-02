import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

def ClearLandscape():
  # set air layer
  # (x1, y1, z1, x2, y2, z2, blockID, blockState)
  mc.setBlocks(-248, 1, -248, 248, 248, 248, 0) 
  # set layer of lava
  mc.setBlocks(-248, -1, -248, 248, -1, 248, 57)
  # set layer of obsidian
  mc.setBlocks(-248, 0, -248, 248, 0, 248, 49)

mc.postToChat("Altering landscape...")
ClearLandscape()
