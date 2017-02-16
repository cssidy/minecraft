#! /usr/bin/python

from mcpi.minecraft import Minecraft
import mcpi.block as block
from math import *

mc = Minecraft.create()

colors = [14,1,4,5,3,11,10]
height = 50

pos = mc.player.getTilePos()
x = pos.x()
y = pos.y()

mc.setBlocks(-64,x,y,64, height + len(colors), 0,0)
for x in range(0, 120):
    for colourindex in range(0, len(colors)):
        y = sin((x / 128.0) * pi) * height + colourindex
        mc.setBlock(x-64, int(y), 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])
