f = open("mcpi.dump")
ass = f.read().split('\n')
f.close()

ass1 = []

for i in ass:
    i_split = i.split(" ")
    if "<UNDEFINED>" in i_split or "..." in i_split:
        continue
    if i_split[:7] == ['']*7:
        temp = ' '.join(i_split[8:]).replace('\t', ' ')
        ass1.append(temp)
print(ass1)