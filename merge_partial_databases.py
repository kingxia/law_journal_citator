import os, sqlite3
from lib.constants import *

def create_database(dst):
    if os.path.exists(dst):
        os.remove(dst)
    db = sqlite3.connect(dst)
    cursor = db.cursor()
    cursor.execute(CREATE_CITES_TABLE)
    cursor.execute(CREATE_NEXT_IDS_TABLE)
    cursor.execute(INSERT_NEXT_ID % (0, 1000))
    db.commit()
    db.close()

def get_partial_databases():
    return os.listdir(PARTIALS_PATH)

def merge_databases(dst, src):
    write_to = sqlite3.connect(dst)
    read_from = sqlite3.connect(src)

    read_cursor = read_from.cursor()
    read_cursor.execute('SELECT * FROM citations')
    cite_data = read_cursor.fetchall()
    read_from.close()

    write_cursor = write_to.cursor()
    write_cursor.execute('SELECT * FROM nextIds WHERE id = 0')
    next_id = write_cursor.fetchall()[0][1]
    
    for row in cite_data:
        write_cursor.execute(INSERT_CITATION % (
            row[0] + next_id, row[1], row[2], row[3], row[4],
            row[5].replace('"', '""'), row[6], row[7], row[8], row[9],
            row[10]))
    write_cursor.execute('UPDATE nextIds SET nextId = %d WHERE id = 0' % (next_id + len(cite_data)))

    write_to.commit()
    write_to.close()

def main():
    create_database(DATABASE_PATH)
    dbs = get_partial_databases()
    for db in dbs:
        merge_databases(DATABASE_PATH, PARTIALS_PATH + db)

if __name__ == '__main__':
    main()
