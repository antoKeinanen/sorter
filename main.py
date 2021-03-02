from os import listdir, walk, mkdir, replace
from os.path import isfile, join
import pathlib

path = input("name of root folder: ")

dirs = [x[0] for x in walk(path) if "--" not in x[0]]
files = [join(d, f) for d in dirs for f in listdir(d) if isfile(join(d, f))]
types = []

for f in files:
    t = pathlib.Path(f).suffix.replace(".", "")
    if t not in types:
        types.append(t)


for t in types:
    try:
        mkdir(join(path, t))
    except FileExistsError:
        print(f"folder {t} already exists!")

for f in files:
    replace(f, join(path, join(pathlib.Path(f).suffix.replace(".", ""), pathlib.Path(f).name)))
