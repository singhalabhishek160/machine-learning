name = open("mbox-short.txt")
coll= dict()
for lines in name:
    if lines.startswith("From"):
        word=lines.split();
        if len(word)>1
        	if word[2] not in coll:
            	coll[word[2]]=1
        	else:
            	word[2]=coll.get(word[2],0)+1
            

max_count=0

for a in coll:
    if coll[a]>max_count:
        max_count = coll[a]

print(coll[max_count],max_count)
