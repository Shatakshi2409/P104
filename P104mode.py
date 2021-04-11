import csv
from collections import Counter
with open('SOCR.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(float(num))

data=Counter(newdata)
modedataforrange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modedataforrange['50-60']+=occurence
    elif 60<float(height)<70:
        modedataforrange['60-70']+=occurence
    elif 70<float(height)<80:
        modedataforrange['70-80']+=occurence

moderange,modeoccurence=0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split('-')[0]),int(range.split('-')[1])],occurence

mode=float((moderange[0]+moderange[1])/2)
print(f'mode:{mode:2f}')