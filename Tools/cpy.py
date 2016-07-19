import shutil
cpy = shutil.copyfile
origin = "pic.png"
for i in range(4001,4066 + 1) :
	name = "wp_icon_%d.png" %i
	cpy(origin,name)
