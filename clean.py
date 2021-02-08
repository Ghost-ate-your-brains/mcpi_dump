output = []

with open('mcpi.dump') as f:
    dump = f.read().split('\n')
    for i in dump:
        i_split = i.split()
        if "<UNDEFINED>" in i_split or i_split == ['...']:
            continue
        i_formatted = [j.replace('\t', '') for j in i_split if j not in ['', ';']]
        only_mnemonic = i_formatted[2:]
        print(only_mnemonic)
        output.append(only_mnemonic)

print(output)
