import os,json

def list_dir():
    directories={i:0 for i in os.listdir() if os.path.isdir(f"./{i}") and (not i.startswith("."))}
    return directories

def count_blobs(directories):
    total=0
    for i in directories.keys():
        directories[i]=sum(1 for j in os.listdir(f"./{i}") if os.path.isfile(f"./{i}/{j}") and j.endswith(".py"))
        total+=directories[i]
    directories["total_solved"]=total


if __name__=="__main__":
    directories=list_dir()
    count_blobs(directories)
    with open("progress.json", "w", encoding="utf-8") as progress_file:
        json.dump(directories, progress_file)




    