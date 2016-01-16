def main():
    #test the PathMap function
    print(pathMap(1,2,1,1,raceAns = "Dwarf",classAns="Fighter"))

#define the path for the choose your own adventure game
def pathMap(*args,**kwargs):
    pathDictionary = kwargs
    pathDictionary["currentPath"]=kwargs.get("currentPath",[0])
    pathDictionary["raceAns"]=kwargs.get("raceAns","Human")
    pathDictionary["classAns"]=kwargs.get("classAns","Fighter")
    pathDictionary["gold"]=kwargs.get("gold",100)
    pathDictionary["life"]=kwargs.get("life",100)

    #if lenght is one this is the inital path
    if len(pathDictionary["currentPath"]) == 1:
        pathDictionary["advText"] = "Congratulations! You have just graduated from adventurer school! Time to go off on your first adventure. To your left is a bright and sunny path. Birds chirp and occassionally squirells dart to and fro. To your right is a bridge that goes over a raging river. On the other side you can see houses and a farm. Finally, off in the trees you can see the opening to a cave."
        pathDictionary["afill"] = "Go down the path"
        pathDictionary["bfill"] = "Go over the bridge"
        pathDictionary["cfill"] = "Go into the dark and scary cave"

    return(pathDictionary)

if __name__ == '__main__': main()