from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = 9

x,y,z = mc.player.getPos()

mc.setBlocks(x+1,y,z,x+5,y,z+4, blocks)
mc.setBlocks(x+2,y+1,z+1,x+4,y,z+3, blocks)
mc.setBlocks(x+3,y+2,z+2,x+3,y,z+2, blocks) 