import json
import time


def reformat_dump(file):
    file_dump = open(file)
    dump_read = file_dump.read().split('\n')
    file_dump.close()
    temp = {}

    for line in dump_read:
        i_split = line.split()
        if "<UNDEFINED>" in i_split or bool(i_split) is False or i_split == ['...']:
            continue
        i_formatted = [j.replace('\t', '') for j in i_split if j not in ['', ';']]
        only_mnemonic = i_formatted[2:]
        id = str(i_formatted[0].replace(':', ''))
        temp[id] = only_mnemonic

    return temp


def write_json(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def read_json_line(path):
    with open(path) as f:
        dump = json.load(f)
        for i in dump:
            print(f'Работаю со строкой: {i}, значение: {dump[i]}')
            time.sleep(0.1)


def program():
    dump_reformat = reformat_dump('mcpi.dump')
    write_json(path='output.json', data=dump_reformat)


read_json_line('output.json')
