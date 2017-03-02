import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()


mc.saveCheckpoint()
mc.postToChat("Checkpoint saved.")

# mc.restoreCheckpoint()
