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

total=dict([('advanced_techniques',25), ('constr_problems',8), ('graph_algorithms',36), ('additional_problemsI',30), 
            ('range_queries',25), ('bitwise_ops',11), ('introductory_problems',24), ('dynamic_programming',23), 
            ('interactive_problems',6),('slidingWindowProblems',11), ('advanced_graphProblems',28), 
            ('counting_problems',18), ('string_algorithms',21), ('maths',37), ('tree_algorithms',16), 
            ('geometry',16), ('additional_problemsII',30), ('sorting_searching',35),('total_solved',400)])

if __name__=="__main__":
    directories=list_dir()
    count_blobs(directories)

    jsonvalues={i:str(directories[i]) + "/" + str(total[i]) for i in directories}
    with open("progress.json", "w", encoding="utf-8") as progress_file:
        json.dump(jsonvalues, progress_file)




    