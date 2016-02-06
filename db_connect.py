import sqlite3

global conn

conn = sqlite3.connect('cyoa.db')

def createTable():
    conn.execute('''CREATE TABLE class_tbl (class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                class TEXT));
                                                    ''')

    conn.execute('''CREATE TABLE race_tbl(race_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            race TEXT);''')

    conn.execute('''CREATE TABLE adv_tbl (adv_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            class_id INTEGER REFERENCES class_tbl(class_id) ON UPDATE CASCADE,
                                            race_id INTEGER REFERENCES race_tbl(race_id) ON UPDATE CASCADE,
                                            path VARCHAR NOT NULL,
                                            advText VARCHAR NOT NULL,
                                            choiceA VARCHAR NOT NULL,
                                            choiceB VARCHAR NOT NULL,
                                            choiceC VARCHAR NOT NULL);''')

def addRace(RACE):
    val_str = ('{}'.format(RACE))
    conn.execute("INSERT INTO race_tbl (race) VALUES ('{}');".format(val_str))
    conn.commit()

def addClass(CLASS):
    val_str = ('{}'.format(CLASS))
    conn.execute("INSERT INTO class_tbl (class) VALUES ('{}');".format(val_str))
    conn.commit()

def addAdventure(**kwargs):
    val_dict = kwargs
    CLASS_ = val_dict.get('class_')
    RACE = val_dict.get('race')
    PATH = val_dict.get('path')
    ADVTEXT = val_dict.get('advText')
    A = val_dict.get('a')
    B = val_dict.get('b')
    C = val_dict.get('c')
    #skip class or race if the value is null. Not every path will have variations depending on the class and race
    conn.execute("INSERT INTO adv_tbl (path, advText, choiceA, choiceB, choiceC) \
                    VALUES ('{}','{}','{}','{}','{}');".format(PATH, ADVTEXT, A, B, C))
    conn.commit()

def getChar(**kwargs):
    sql = "SELECT {0}_id FROM {0}_tbl WHERE {0} = '{1}' LIMIT 1;".format(
        kwargs.get("tableName","class"),
        kwargs.get("fieldName"))

    results = conn.execute(sql)
    for result in results:
        for r in result:
            return r

def getPath(*args, **kwargs):
    """

    :rtype: object
    """

    #set variables to use in query
    currentPath = args
    pathDictionary = kwargs
    pathDictionary["gold"]=kwargs.get("gold",100)
    pathDictionary["life"]=kwargs.get("life",100)

    strPath = ','.join(map(str, currentPath))

    classId = getChar(tableName= "class",fieldName=pathDictionary.get("classAns"))
    raceId   = getChar(tableName="race",fieldName=pathDictionary.get('raceAns'))
    print("Race id {}, class id {}".format(raceId,classId))

    #SQL Query creation
    sql = "SELECT * FROM adv_tbl WHERE path = '{}';".format(strPath)
    print(sql)
    results = conn.execute(sql)

    for r in results:

        if r[1] == classId and r[2] == raceId:
            print("match both")
            pathDictionary["advText"]= r[4]
            pathDictionary["afill"] = r[5]
            pathDictionary["bfill"] = r[6]
            pathDictionary["cfill"] = r[7]
            return pathDictionary

        if r[1] == classId or r[2] == raceId:
            print("match one")
            pathDictionary["advText"]= r[4]
            pathDictionary["afill"] = r[5]
            pathDictionary["bfill"] = r[6]
            pathDictionary["cfill"] = r[7]
            return pathDictionary

        if r[1]==None and r[2] == None:
            print("match none")
            pathDictionary["advText"]= r[4]
            pathDictionary["afill"] = r[5]
            pathDictionary["bfill"] = r[6]
            pathDictionary["cfill"] = r[7]
            return pathDictionary

        else:
            print("no match")


def main():
    '''    parameterList = dict(path = "",
                        advText = "",
                        a = "",
                        b = "",
                        c = "",
                        class_= 0,
                        race = 0)
    '''
    #    addAdventure(**parameterList)

    #test getPath
    getPath((0, 1), raceAns = "Elf", classAns = "Fighter")


    #conn.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    conn.close()

if __name__=='__main__': main()