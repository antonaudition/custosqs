import sqlite3
import pickle


# My SQL is not enough :)
class SqLiteDriver:
    table_name = 'bcrypt_table'
    c1n = "md5sum"
    c2n = "rounds"
    c3n = "bcrypt"

    def __init__(self, sqlite_file):
        self.conn = sqlite3.connect(sqlite_file)
        c = self.conn.cursor()

        # Creating a new SQLite table if it doesn't exist
        c.execute('CREATE TABLE IF NOT EXISTS {tn}({c1n} {c1t}, {c2n} {c2t}, {c3n} {c3t}, PRIMARY KEY({c1n}, {c2n}))'
                  .format(tn=self.table_name, c1n=self.c1n, c1t="TEXT NOT NULL", c2n=self.c2n, c2t="INTEGER NOT NULL",
                          c3n=self.c3n, c3t="TEXT"))

    def close(self):
        self.conn.close()

    def insert(self, md5_sum, rounds, bcrypt_value):
        c = self.conn.cursor()
        c.execute('INSERT INTO {tn} ({c1n}, {c2n}, {c3n}) VALUES ({c1v}, {c2v}, {c3v})'
                  .format(tn=self.table_name, c1n=self.c1n, c1v=md5_sum, c2n=self.c2n, c2v=rounds,
                          c3n=self.c3n, c3v=bcrypt_value))
        self.conn.commit()

    def lookup(self, md5_sum, rounds):
        pass


# mock originally just for testing
class PickleDriver:
    def __init__(self, pickle_file):
        self.pickle_file = pickle_file
        try:
            self.store = pickle.load(open(pickle_file, "rb"))
        except IOError:
            self.store = {}

    def close(self):
        pickle.dump(self.store, open(self.pickle_file, "wb"))

    def insert(self, md5_sum, rounds, bcrypt_value):
        self.store["{}_{}".format(md5_sum, rounds)] = (md5_sum, rounds, bcrypt_value)

    def lookup(self, md5_sum, rounds):
        key = "{}_{}".format(md5_sum, rounds)
        if key in self.store:
            return self.store[key][2]
        else:
            return None
