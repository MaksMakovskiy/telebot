import re
import sqlite3
from sqlite3.dbapi2 import Cursor

from numpy import true_divide


class DataCrude():
    def __init__(self) -> None:
        self.sqlconn = sqlite3.connect(
            "base.db", check_same_thread=False)
        self.fether = self.sqlconn.cursor()
        self.players = {}
        self.DoDIctUsers()


    def message_chek(self, id):
        self.DoDIctUsers
        if id in self.players:
            return True
        else:
            return False

    def PrintUserToBase(self, id, prim=0):
        if id not in self.players:
            self.fether.execute(
                f"INSERT INTO player (id, primogem) VALUES ('{id}', '{prim}');")
            self.sqlconn.commit()

    def newplayerfuch(self, id):
        if self.message_chek(id) == True:
            return True
        else:
            self.PrintUserToBase(id)
            return False

    def DoDIctUsers(self):
        self.fether.execute("SELECT * FROM player;")
        record = self.fether.fetchall()

        for i in range(len(record)):
            self.players[record[i][0]] = {"primogem": record[i][1], "lastuse": record[i][2]}


       

    def ConnClose(self):
        self.sqlconn.close()


b = DataCrude()
