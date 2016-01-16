def main():
    #test the PathMap function
    print(pathMap(0,1,1,1, raceAns = "Dwarf",classAns="Fighter"))

#define the path for the choose your own adventure game
def pathMap(*args,**kwargs):
    currentPath = args
    pathDictionary = kwargs

    pathDictionary["raceAns"]=kwargs.get("raceAns","Human")
    pathDictionary["classAns"]=kwargs.get("classAns","Fighter")
    pathDictionary["gold"]=kwargs.get("gold",100)
    pathDictionary["life"]=kwargs.get("life",100)

    #if lenght is one this is the inital path
    pathDictionary["advText"] = "Congratulations! You have just graduated from adventurer school! Time to go off on your first adventure. To your left is a bright and sunny path. Birds chirp and occassionally squirells dart to and fro. To your right is a bridge that goes over a raging river. On the other side you can see houses and a farm. Finally, off in the trees you can see the opening to a cave."
    pathDictionary["afill"] = "Go down the path"
    pathDictionary["bfill"] = "Go over the bridge"
    pathDictionary["cfill"] = "Go into the dark and scary cave"

    if len(currentPath)==2:
        if currentPath[1] == 1:
            pathDictionary["advText"] = "Day slowly turns into night as you leisurely walk down the path. You camp for the night in a pleasant stand of trees. During the night you are awoken by a horrible screetching and a hulking shadow falls over your tent!"
            if pathDictionary["classAns"] == 'Wizard':
                pathDictionary["afill"] = "Blast it with a fireball!"
                pathDictionary["bfill"] = "Magic missle the darkness!"
                pathDictionary["cfill"] = "Crawl quietly out of the tent and run!"
            if pathDictionary["classAns"] == 'Rogue':
                pass
            if pathDictionary["classAns"] == 'Priest':
                pass
            if pathDictionary["classAns"] == 'Fighter':
                pathDictionary["afill"] = "Grab your axe."
                pathDictionary["bfill"] = "Grab your shield."
                pathDictionary["cfill"] = "Grab your backpack."
        if currentPath[1]==2:
            pass
        if currentPath[1]==3:
            pass

    return(pathDictionary)

if __name__ == '__main__': main()