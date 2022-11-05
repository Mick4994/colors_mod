import os
import cv2

def new_block():
    f = open('new_block.txt','w')
    texture_file = os.listdir('./texture/')
    str_ahead = 'public static final Block '
    # str_end = ' = new Block(AbstractBlock.Settings.of(Material.STONE).strength(-1.0F, 3600000.0F).dropsNothing());'
    str_end = ' = new Block(AbstractBlock.Settings.of(Material.STONE).strength(-1.0F, 3600000.0F));'
    for name in texture_file:
        line1 = str_ahead + name[:-4].upper() + str_end + '\n'
        f.write(line1)
        # line2 = "public static final BlockItem " + name[:-4].upper() + "_ITEM = new BlockItem(" + name[:-4].upper() + ", new FabricItemSettings());\n"
        # f.write(line2)
    f.close()

def reg_block():
    f = open('reg_block.txt','w')
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        # line1 = "Registry.register(Registry.ITEM, new Identifier(MOD_ID, " + '"' + name[:-4] + '"' + "), " + name[:-4].upper() + "_ITEM);\n"
        # f.write(line1)
        line2 = "Registry.register(Registry.BLOCK, new Identifier(MOD_ID, " + '"' + name[:-4] + '"' + "), " + name[:-4].upper() + ");\n"
        f.write(line2)
    f.close()

def icon():
    img = cv2.imread('src_icon.jpg')
    img = cv2.resize(img,(128,128))
    cv2.imwrite('icon.png',img)

def lang():
    f = open('lang.txt','w')
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        line = '"'+"item.colors_mod." + name[:-4] + '":' + '"' + name[5:-4] + '",\n'
        f.write(line)
    f.close()

def block_json():
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        lines = []
        lines.append("{\n")
        lines.append('  "parent": "minecraft:block/cube_all",\n')
        lines.append('  "textures": {\n')
        lines.append('    "all": "colors_mod:block/' + name[:-4] +'"\n')
        lines.append('  }\n')
        lines.append('}\n')
        f = open("./block_json/" + name[:-4] + ".json", "w")
        f.writelines(lines)
        f.close()

def block_item_json():
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        lines = []
        lines.append("{\n")
        lines.append('  "parent": "colors_mod:block/' + name[:-4] + '"\n')
        lines.append('}\n')
        f = open("./block_item_json/" + name[:-4] + ".json", "w")
        f.writelines(lines)
        f.close()

def blockstate():
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        lines = []
        lines.append("{\n")
        lines.append('  "variants": {\n')
        lines.append('    "":\n')
        lines.append('    {\n')
        lines.append('      "model": "colors_mod:block/' + name[:-4] +'"\n')
        lines.append('    }\n')
        lines.append('  }\n')
        lines.append('}\n')
        f = open("./blockstate_json/" + name[:-4] + ".json", "w")
        f.writelines(lines)
        f.close()

def rename():
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        srcname = name
        name = name.replace('-','_')
        os.rename('./texture/' + srcname,'./texture/'+ name)

def block_name():
    f = open('block_list.txt','w')
    texture_file = os.listdir('./texture/')
    for name in texture_file:
        line = '"' + name[:-4] + '",\n'
        f.write(line)
    f.close()

# reg_block()
# new_block()
# icon()
# lang()
# block_json()
# block_item_json()
# blockstate()
# rename()
block_name()


