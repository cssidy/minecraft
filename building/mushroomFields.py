import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

def ClearLandscape():
  # set air layer
  # (x1, y1, z1, x2, y2, z2, blockID, blockState)
  mc.setBlocks(-248, 1, -248, 248, 248, 248, 0) 
  # set layer of podzal
  mc.setBlocks(-248, 0, 0, 248, -3, 248, 3, 2)
  # set layer of mushrooms
  # mc.setBlocks(-248, 0, -248, 248, 0, 248, 40)

mc.postToChat("Altering landscape...")
ClearLandscape()
