import tempfile
import os


class File:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write('')
        with open(self.filename, 'r') as f:
            self.ob = f.read()
        self.current = 0


    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filename, 'r') as f:
            f.seek(self.current)
            s = f.readline()
            if(s):
                self.current = f.tell()
            else:
                raise StopIteration()
        return s


    def write(self, string):
        with open(self.filename, 'w') as f:
            f.write(string)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()


    def __add__(self, obj):
        storage_path = os.path.join(tempfile.gettempdir(),'file.txt')

        with open(self.filename, 'r') as f:
            a1 = f.read()

        with open(obj.filename, 'r') as f:
            a2 = f.read()

        a = a1 + a2
        with open(storage_path, 'w') as f:
            print(type(f))
            f.write(a)
        C = File(storage_path)
        return C

    def __str__(self):
        return '{}'.format(self.filename)
