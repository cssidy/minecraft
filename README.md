# Minecraft Hacking w/ Python & Pi

What's the best way to learn Python and play video games at the same time? Raspberry Pi! The aim of this code is to demonstrate basic syntax and calls to the Minecraft API and how to build inspiring structures in your own Minecraft world.

## Table of Contents

* Code Example
* Prerequisites
* Installation
* License
* Acknowledgments

## Code Example

The code in this repository is Python 3.5. However, there are other languages that are compatible with Minecraft: Pi Edition including:

1. Java
2. [Node.js](https://npmjs.org/package/minecraft-pi)
3. [Smalltalk](http://croquetweak.blogspot.ca/2013/02/smalltalk-bindings-for-minecraft-pi.html)
4. [Ruby](https://github.com/nhajratw/minecraft_api)
5. [Haskell](https://github.com/DougBurke/hmcpi)

The aim is to learn how to connect to the Minecraft API and understand common methods that allow changing block types, setting and removing blocks, and changing the player's tile coordinate position. For example, the following script changes the player's position in the world:

```
# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x, y, and z variables to represent coordinates
x = 10
y = 110
z = 12

# Change the player's position
mc.player.setTilePos(x, y, z)
```

## Prerequisites

To experiment with these programs, you will need to have a compatible version of Python 3 (Python 3.5 is used here) and Minecraft: Pi Edition installed on your system. You will also need an IDE. It does not have to be complex; the Python IDLE console is suitable for interacting with the game. If you are using the Raspberry Pi 3 Model B, you're all set.

## Installation And Usage

### Check Software Versions

Make sure you have all prerequisites installed:

 ``` 
 python3 --version
 git --version
 ```
 

### Download GitHub Repository

In the command line, navigate to the directory that you desire to hold the source code. Then recreate the repository.

```
git clone https://github.com/cssidy/minecraft-hacks
```

### Open Scripts In IDLE

Have the Python IDLE console open while you play Minecraft: Pi Edition. Press <tab> on your keyboard to release the cursor from the Pi and enter your scripts directly into the IDLE console. Press <enter> to put them into effect. For some scripts, it is more efficient to create a .py file and import it into the console to be run.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details. All scripts are created by Cassidy Brooke, except scripts that are marked otherwise.

## Acknowledgments

Some of these scripts are borrowed and/or derived from the book Learn To Program With Minecraft: Transform Your World With The Power of Python, written by Craig Richardson. This book can be purchased as an eBook or paperback from [No Starch Press](https://www.nostarch.com/programwithminecraft).
