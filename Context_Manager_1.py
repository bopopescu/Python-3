import os
from contextlib import contextmanager

### Open File
f = open(r"\APdist1.csv","w")
f.write("a,b")
f.close()



class Open_File():

    def __init__(self, path, mode):  # accept arguments
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open_File(r"\APdist1.csv","w") as f:
    f.write("s,d,d")


##Change Directory

cwd = os.getcwd()
os.chdir(r"C:\Users\86753")
print(os.listdir())
os.chdir(cwd)
print(os.listdir())


with Ctx_open (r"\APdist2.csv", "w") as d:
     d.write("s,d,d")


cwd = os.getcwd()
os.chdir(r"C:\Users\86753")
print(os.listdir())
os.chdir(cwd)
print(os.listdir())

@contextmanager
def ch_dir(new_dir):
    try:
        cwd1 =os.getcwd()
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(cwd1)

with ch_dir(r"C:\Users\86753"):
    print(os.listdir())

print(os.getcwd())
