from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = 44
x,y,z = mc.player.getPos()

mc.setBlocks (x+1,y+1,z+1, x+300, y+300, z+300, blocks)  