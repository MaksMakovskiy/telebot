from doctest import FAIL_FAST
import sqlite3


class DataCrude():
    def __init__(self) -> None:
        self.sqlconn = sqlite3.connect(
            "base.db", check_same_thread=False)
        self.fether = self.sqlconn.cursor()


    def CheakClanName(self, ClanName) -> True|False:
        self.fether.execute(
            f"SELECT Name FROM Clans WHERE name='{ClanName}'"
        )
        ClanInfo = self.fether.fetchall()
        if ClanInfo != []:    
            if ClanName == ClanInfo[0][0]:
                return True         
            else:
                return False
        else:
            return False


    def CheakClanLider(self, ClanName) -> True|False:
        if self.CheakClanName(ClanName) == True: 
            self.fether.execute(
                f"SELECT Lider FROM Clans WHERE name='{ClanName}'"
            )
            return self.fether.fetchall()[0][0]    

    def CreateClan(self, ClanName, LiderName) -> True|False: 
        if self.CheakClanName(ClanName) == False:
            self.fether.execute(
                    f"INSERT INTO Clans (Name, Lider) VALUES ('{ClanName}', '{LiderName}');")
            self.sqlconn.commit()
            self.fether.execute(f'''
                CREATE TABLE "{ClanName}" (
	            Id	INTEGER NOT NULL UNIQUE,
	            Name	TEXT NOT NULL UNIQUE,
	            PRIMARY KEY(Id)
            )''')
            self.sqlconn.commit()
            self.fether.execute(
                    f"INSERT INTO {ClanName} (Name) VALUES ('{LiderName}');")
            self.sqlconn.commit()    
            return True
        else:
            return False


    def DeleteClan(self, ClanName, LiderName) -> True|False:
        if self.CheakClanName(ClanName) == True:
            if LiderName == self.CheakClanLider(ClanName):
                self.fether.execute(
                        f"DELETE FROM Clans WHERE Name='{ClanName}';")
                self.sqlconn.commit()
                self.fether.execute(
                        f"DROP TABLE {ClanName};")
                self.sqlconn.commit()  
                return True  
            else:
                return False
        else:
            return False


    def ConnClose(self):
        self.sqlconn.close()


b = DataCrude()
