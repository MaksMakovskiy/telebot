import sqlite3


class DataCrude():
    def __init__(self) -> None:
        self.sqlconn = sqlite3.connect(
            "base.db", check_same_thread=False)
        self.fether = self.sqlconn.cursor()
        self.players = {}


    def PrintUserToBase(self, id, prim=0):
        if id not in self.players:
            self.fether.execute(
                f"INSERT INTO player (id, primogem) VALUES ('{id}', '{prim}');")
            self.sqlconn.commit()


    def ConnClose(self):
        self.sqlconn.close()


b = DataCrude()
