# Minecraft API Cheatsheet
The following is a quick reference guide for the Minecraft Python API Library that you may need.

![Controls reference](https://arghbox.files.wordpress.com/2013/07/minecraft-pi-controls.png "Controls reference")

## Creating Blocks

### Of a specific type
```
blockObj = block.Block(id)
```

### Of a specific type and data value
```
blockObj = block.Block(id, data)
```

### Block IDs:

* AIR                 = Block(0)
* STONE               = Block(1)
* GRASS               = Block(2)
* DIRT                = Block(3)
* COBBLESTONE         = Block(4)
* WOOD_PLANKS         = Block(5)
* SAPLING             = Block(6)
* BEDROCK             = Block(7)
* WATER_FLOWING       = Block(8)
* WATER               = WATER_FLOWING
* WATER_STATIONARY    = Block(9)
* LAVA_FLOWING        = Block(10)
* LAVA                = LAVA_FLOWING
* LAVA_STATIONARY     = Block(11)
* SAND                = Block(12)
* GRAVEL              = Block(13)
* GOLD_ORE            = Block(14)
* IRON_ORE            = Block(15)
* COAL_ORE            = Block(16)
* WOOD                = Block(17)
* LEAVES              = Block(18)
* GLASS               = Block(20)
* LAPIS_LAZULI_ORE    = Block(21)
* LAPIS_LAZULI_BLOCK  = Block(22)
* SANDSTONE           = Block(24)
* BED                 = Block(26)
* COBWEB              = Block(30)
* GRASS_TALL          = Block(31)
* WOOL                = Block(35)
* FLOWER_YELLOW       = Block(37)
* FLOWER_CYAN         = Block(38)
* MUSHROOM_BROWN      = Block(39)
* MUSHROOM_RED        = Block(40)
* GOLD_BLOCK          = Block(41)
* IRON_BLOCK          = Block(42)
* STONE_SLAB_DOUBLE   = Block(43)
* STONE_SLAB          = Block(44)
* BRICK_BLOCK         = Block(45)
* TNT                 = Block(46)
* BOOKSHELF           = Block(47)
* MOSS_STONE          = Block(48)
* OBSIDIAN            = Block(49)
* TORCH               = Block(50)
* FIRE                = Block(51)
* STAIRS_WOOD         = Block(53)
* CHEST               = Block(54)
* DIAMOND_ORE         = Block(56)
* DIAMOND_BLOCK       = Block(57)
* CRAFTING_TABLE      = Block(58)
* FARMLAND            = Block(60)
* FURNACE_INACTIVE    = Block(61)
* FURNACE_ACTIVE      = Block(62)
* DOOR_WOOD           = Block(64)
* LADDER              = Block(65)
* STAIRS_COBBLESTONE  = Block(67)
* DOOR_IRON           = Block(71)
* REDSTONE_ORE        = Block(73)
* SNOW                = Block(78)
* ICE                 = Block(79)
* SNOW_BLOCK          = Block(80)
* CACTUS              = Block(81)
* CLAY                = Block(82)
* SUGAR_CANE          = Block(83)
* FENCE               = Block(85)
* GLOWSTONE_BLOCK     = Block(89)
* BEDROCK_INVISIBLE   = Block(95)
* STONE_BRICK         = Block(98)
* GLASS_PANE          = Block(102)
* MELON               = Block(103)
* FENCE_GATE          = Block(107)
* GLOWING_OBSIDIAN    = Block(246)
* NETHER_REACTOR_CORE = Block(247)

### Block Data Types:

WOOL

* White
* Orange
* Magenta
* Light Blue
* Yellow
* Lime
* Pink
* Grey
* Light grey
* Cyan
* Purple
* Blue
* Brown
* Green
* Red
* Black

WOOD

* Oak (up/down)
* Spruce (up/down)
* Birch (up/down)

SAPLING

* Oak
* Spruce
* Birch

GRASS_TALL

* Shrub
* Grass
* Fern

TORCH

* Pointing east
* Pointing west
* Pointing south
* Pointing north
* Facing up

STONE_BRICK

* Stone brick
* Mossy stone brick
* Cracked stone brick
* Chiseled stone brick

STONE_SLAB / STONE_SLAB_DOUBLE

* Stone
* Sandstone
* Wooden
* Cobblestone
* Brick
* Stone Brick
