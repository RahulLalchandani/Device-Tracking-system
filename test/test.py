import sqlite3


def test_run():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()

    print("\n devices table:")
    query = "select * from devices"
    res = cursor.execute(query)
    print(res.fetchall())

    print("\n labs table:")
    query = "select * from labs"
    res = cursor.execute(query)
    print(res.fetchall())

    print("\n belongs table:")
    query = "select * from belongs"
    res = cursor.execute(query)
    print(res.fetchall())

    print("\n logs table")
    query = "select * from log"
    res = cursor.execute(query)
    print(res.fetchall())

    print("\n Login Table")
    query = "select * from login"
    res = cursor.execute(query)
    print(res.fetchall())


if __name__ == "__main__":
    test_run()
