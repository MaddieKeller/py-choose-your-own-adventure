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

def main():
    parameterList = dict(path = "",
                        advText = "",
                        a = "",
                        b = "",
                        c = "",
                        class_= 0,
                        race = 0)

    addAdventure(**parameterList)

    #conn.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    conn.close()

if __name__=='__main__': main()