import sqlite3

class dbopen(object):
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """
    def __init__(self, path):
        self.path = path
        #self.conn = None
        #self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    with dbopen('./sample.db') as c:
        #c.execute("CREATE TABLE seekmap (id text, offset int, length int)")
        c.execute("INSERT INTO seekmap VALUES ('a', 0, 2000)")
        c.execute("INSERT INTO seekmap VALUES ('b', 2000, 3000)")
        c.execute("SELECT * FROM seekmap")
        result = c.fetchall()
        print(result)
        # [(u'a', 0, 2000), (u'b', 2000, 3000)]
