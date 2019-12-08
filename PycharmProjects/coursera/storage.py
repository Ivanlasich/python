import os
import tempfile
import json
import argparse

def write_json(key, val):

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        try:
            data = json.load(f)
        except:
            data = {}
    try:
        data[key].append(val)
    except:
        data[key] = []
        data[key].append(val)

    with open(storage_path, 'w') as f:
        json.dump(data, f, indent = 2, ensure_ascii= False)


def pop_json(key):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        try:
            data = json.load(f)
        except:
            data = dict()
    try:
        for i in range(len(data[key])):
          if i!=len(data[key])-1:  print(data[key][i], end = ", ")
          else: print(data[key][i])
    except:
        print("")

    with open(storage_path, 'w') as f:
        json.dump(data, f, indent = 2, ensure_ascii= False)


def read_json():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', nargs='?')
    parser.add_argument('--val', nargs='?')
    args = parser.parse_args()

    d={}
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            json.dump(d, f)
    with open(storage_path, 'r') as f:
        if not f.read():
            with open(storage_path, 'w') as f:
                json.dump(d, f)




    if args.key and args.val:
          write_json(args.key, args.val)
    elif args.key:
          pop_json(args.key)
    else:
       print('')
#    pop_json('key')
#    read_json()