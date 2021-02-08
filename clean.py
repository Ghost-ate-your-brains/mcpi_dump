f = open("mcpi.dump")
ass = f.read().split('\n')
f.close()
ass1 = []
n = 0
for i in ass:
    ii = i.split(" ")
    if "<UNDEFINED>" in i or "..." in i or len(ii) < 8:
        continue
    lenth = len(ii)
    _car = 0
    _temp = ' '.join(ii[-(lenth-4):])
    print(ii)
    ass1.append(_temp)
    n += 1