from PIL import Image
import os
import pandas
folder=r"C:\Users\MY598RL\Desktop\New folder"

names=os.listdir(folder)
result=[]
print(names)
path=os.path.join(folder,names[0])
names.pop(0)
output=Image.open(path)
output=output.resize((1970,1110),Image.LANCZOS)
if output.mode!="RGB":
    output=output.convert('RGB')
for name in names:
    path=os.path.join(folder,name)
    IM=Image.open(path)
    IM=IM.resize((1970,1110),Image.Resampling.LANCZOS)
    if IM.mode!="RGB":
        IM=IM.convert('RGB')
    result.append(IM)
output.save(r"C:\Users\MY598RL\Desktop\New folder\1111","pdf",resoulution=100.0,save_all=True,append_images=result)
