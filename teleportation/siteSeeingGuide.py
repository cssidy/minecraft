from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"Home": (2, 0, 4),
                  "Tower": (),
                  "Pyramid": (),
                  "Castle": (),
                }

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2], location[3]
        mc.player.setTilePos(x, y, z)
