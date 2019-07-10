import sqlite3
from tabulate import tabulate

def test_run():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()

    print("\n DEVICES TABLE :")
    query = "select * from devices"
    res = cursor.execute(query)
    print(tabulate(res.fetchall(),headers=('DEVICE ID',
         'DESCRIPTION')))

    print("\n LABS TABLE :")
    query = "select * from labs"
    res = cursor.execute(query)
    print(tabulate(res.fetchall(),headers=('LAB ID',
         'DESCRIPTION')))

    print("\n MASTER DEVICE TABLE :")
    query = "select * from belongs"
    res = cursor.execute(query)
    print(tabulate(res.fetchall(),headers=('LAB ID',
         'DEVICE ID', 'STATUS', 'CRR. LAB')))

    print("\n LOGS TABLE :")
    query = "select * from log"
    res = cursor.execute(query)
    print(tabulate(res.fetchall(),headers=(
         'DEVICE ID', 'CRR. LAB', 'STATUS','TIME STAMP')))


if __name__ == "__main__":
    test_run()
