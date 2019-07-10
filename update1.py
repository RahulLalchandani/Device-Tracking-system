import sqlite3
from ardRfid import run
from test import test_run
from datetime import datetime

db = sqlite3.connect('data.db')
cursor = db.cursor()
lab_id = 1


def get_lab(id1):
    query = "select * from belongs where device_id = ?"
    res = cursor.execute(query, (id1,))
    return res.fetchone()


def enter():
    flag = None
    id1 = run()
    res = get_lab(id1)
    query1 = "update belongs set status = ?, current_lab = ? where device_id = ?"
    if res[0] == lab_id:
        flag = "in"
    else:
        flag = "out"
    cursor.execute(query1, (flag, lab_id, id1))
    query = "INSERT INTO log VALUES (?, ?, ?, ?)"
    cursor.execute(query, (id1, lab_id, "in", datetime.now()))
    db.commit()
    test_run()


def exita():
    id1 = run()
    # res = get_lab(id1)
    # print(res[0])
    query1 = "update belongs set status = ?, current_lab = ? where device_id = ?"
    cursor.execute(query1, ("out", None, id1))
    query = "INSERT INTO log VALUES (?, ?, ?, ?)"
    cursor.execute(query, (id1, None, "out", datetime.now()))
    db.commit()
    test_run()


def main():
    print(f"\nLab {lab_id}")
    inp = int(input("1.Enter\n2.Exit\nYour Selection: "))
    if inp == 1:
        enter()
    elif inp == 2:
        exita()
    else:
        print("invalid input")


if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            break
