#!/usr/bin/python3

# written by Cassidy Brooke
# inspired by Matt Hawkins castle from 2014


# import Minecraft libraries
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
mc.postToChat("Generating castle...")

def CreateCastle():

    height=15
    
    x1 = 5
    x2 = x1
    y1 = 0
    y2 = y1+height
    z1 = 5
    z2 = z1
    ceilingHeight = 5

    # 98 mossy brick, state 1
    castleWallsBlockID = 112
    castleWallsBlockState = 0
    castleFloorBlockID = 5
    
    # bottom floor
    mc.setBlocks(-x1, -1, -z1, x2, 0, z2, castleFloorBlockID)
    # second floor
    mc.setBlocks(-x1, ceilingHeight-1, -z1, x2, (ceilingHeight-1), z2, castleFloorBlockID)
   # third floor
    mc.setBlocks(-x1, (ceilingHeight-1)*2, -z1, x2, (ceilingHeight-1)*2, z2, castleFloorBlockID)
    # roof
    mc.setBlocks(-x1, ceilingHeight*3, -z1, x2, ceilingHeight*3, z2, castleWallsBlockID, castleWallsBlockState)
    
    # creates four walls
    mc.setBlocks(-x1, y1, -z1, x2, y2, -z2, castleWallsBlockID, castleWallsBlockState)
    mc.setBlocks(-x1, y1, -z1, -x2, y2, z2, castleWallsBlockID, castleWallsBlockState)
    mc.setBlocks(x1, y1, z1, -x2, y2, z2, castleWallsBlockID, castleWallsBlockState)
    mc.setBlocks(x1, y1, z1, x2, y2, -z2, castleWallsBlockID, castleWallsBlockState)

  # creates battlements on roof
    for x in range(0,(2 * x1)+ 1, 2):
      mc.setBlock(x1, y1+ceilingHeight*3+1,(x-x1), castleWallsBlockID, castleWallsBlockState) 
      mc.setBlock(-x1, y1+ceilingHeight*3+1,(x-x1), castleWallsBlockID, castleWallsBlockState) 
      mc.setBlock((x-x1), y1+ceilingHeight*3+1,x1, castleWallsBlockID, castleWallsBlockState) 
      mc.setBlock((x-x1), y1+ceilingHeight*3+1,-x1, castleWallsBlockID, castleWallsBlockState)
   
    # create door
    mc.setBlocks(-2, y1+1, z1, 2, y1+2, z2, 0)

    # create ladder
    mc.setBlocks(0, 1, -1, 1, ceilingHeight*3+1, 1, 0)
    mc.setBlocks(1, 0, -1, 1, ceilingHeight*3, -1, castleFloorBlockID)

    # create windows
    for level in range(1, 3):
        CreateWindows(0, (level * 5) + y1+1, x1, "N")
        CreateWindows(0, (level * 5) + y1+1, -x1, "S")
        CreateWindows(-x1, (level * 5) + y1+1, 0, "W")
        CreateWindows(x1, (level * 5) + y1+1, 0, "E")

def CreateWindows(x,y,z,dir):

  if dir=="N" or dir=="S":
    z1=z
    z2=z
    x1=x-2
    x2=x+2

  if dir=="E" or dir=="W":
    z1=z-2
    z2=z+2
    x1=x
    x2=x

  mc.setBlocks(x1,y,z1,x1,y+1,z1,0)
  mc.setBlocks(x2,y,z2,x2,y+1,z2,0) 
  
  if dir=="N":
    a=3
  if dir=="S":
    a=2
  if dir=="W":
    a=0
  if dir=="E":
    a=1

  mc.setBlock(x1, y-1, z1, 114, a)
  mc.setBlock(x2, y-1, z2, 114, a)

    
CreateCastle()
