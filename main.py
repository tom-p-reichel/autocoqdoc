from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("glob_dir",help="directory with built (not installed) packages")

args = parser.parse_args()

globs = list(Path(args.glob_dir).rglob("*.glob"))

args = set()

vfiles = set()

for f in globs:
    vfile = (f.parent/(f.stem+".v"))
    if not vfile.exists():
        continue # not finding this
    with open(f) as fp:
        path = [l[1:] for l in fp.read().split("\n") if l.startswith("F")][0]
    
    args.add(("-Q",str(f.parent),".".join(path.split(".")[:-1]))) 
    
    vfiles.add(str(vfile))

with open("vfiles.txt","w") as f:
    f.write("\n".join(vfiles))

print("--parse-comments --html -d html -g " +" ".join(" ".join(f"\"{y}\"" for y in x) for x in args)+" --files-from vfiles.txt")
