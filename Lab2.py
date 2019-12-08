import os
ListOfFiles=os.listdir("C:/")
print len(ListOfFiles)
print(ListOfFiles[15])
AllFiles = []
for r,d,f in os.walk("C:"):
    for file in f:
        AllFiles.append(os.path.join(file))

for f in AllFiles:
    print(f)


for r,d,f in os.walk("C:"):
    for file in f:
        if '.jpg' in file:
            base=os.path.splitext(file)[0]
            os.rename(file,base + ".png")


